# Weakness Reliability Guideline

Use this guideline to judge whether a weakness raised in a paper review is RELIABLE (well-grounded, paper-specific, actionable) or UNRELIABLE (matching one of the error patterns below).

## Error type table

| Error Type | Explanation |
|---|---|
| Misunderstanding | The reviewer misinterprets claims or ideas presented in the paper, leading to inaccurate or irrelevant comments. |
| Neglect | The reviewer overlooks important details explicitly stated in the paper, resulting in unwarranted questions or critiques. |
| Vague Critique | The review lacks specificity, claiming missing components without clearly identifying what is missing. |
| Out-of-scope | The reviewer suggests additional methods, experiments, or analyses that are beyond the intended scope of the paper. |
| Invalid Criticism | The reviewer's criticism is considered invalid, especially when suggesting impractical experiments or trivializing results. |
| Superficial Review | The reviewer appears to have only skimmed the paper, providing generic or unsupported comments about the presence or absence of weaknesses. |
| Unstated statement | Statements made in the review are not supported by content in the paper. |
| Excessive demands | if the weaknesses are just asking for excessive things that are not necessary for a good paper. |
| Generic comment | weaknesses are just generic comments that can apply to any paper, without really pointing out the specific problems of the paper. |

## Examples per error type

Each example is a real reviewer segment annotated by a human as unreliable, with the human's explanation of why.

### Misunderstanding

*The reviewer misinterprets claims or ideas presented in the paper, leading to inaccurate or irrelevant comments.*

**Example 1**
> Reviewer wrote: But the core technical contribution is just an LM-based reweighting. Methodological nvoelty is a shortage.

Why unreliable: The method in this paper is not only about LM-based reweighting. For example, it has considered efficient generation of diverse prompts.They are the first to extract knowledge graphs of arbitrary relations from LMs.

**Example 2**
> Reviewer wrote: I gather that Transformer-XL uses a form of "top-k" sampling, that is, a generation mode more restricted than a standard (from the pure probabilistic viewpoint) "ancestral sampling". Such restricted sampling (as also beam-search) is known to improve the quality but limit the diversity of the generations. It would be interesting to see if you would obtain the same EBP conclusions with ancestral sampling.

Why unreliable: The authors do not use ancestral sampling

**Example 3**
> Reviewer wrote: This provides evidence that finetuning works more robustly than few-shot prompting, and that explicitly training to handle ambiguity helps generalization performance.

Why unreliable: The authors do not claim that finetuning works more robustly than few-shot prompting.

**Example 4**
> Reviewer wrote: The fact that this prompting fails on logical tasks (section 6) poses serious concerns on its applicability on harder problems other than simple mathematical operations and, therefore, its real-world utility.

Why unreliable: The authors never proposed anything universal. they focus on math reasoning only.

**Example 5**
> Reviewer wrote: Besides, it is well known that meta-learning methods are notoriously hard to tune and can be extremely sensitive to hyperparameter choices. It is hard to tune the framework on a large PLM with a small batch size.

Why unreliable: For hyperparameter setup, they do not perform per-task tuning but use a fixed set of hyperparameters, which works quite well for all tasks.

**Example 6**
> Reviewer wrote: It reads like the most significant contribution is using Google search as the information retriever compared with previous work using other search engines on Wikipedia, etc.

Why unreliable: The major contribution of this work is not using Google search as the retriever. The main contribution of this paper is to leverage the most up-to-date information online, instead of those traditional open-book QA methods. Since the LLM's parametric knowledge and the quick evolution of online knowledge have become more and more popular recently (2023~2024), I think this paper's contribution is also solid at 2021~2022.

**Example 7**
> Reviewer wrote: It is not clear if the external knowledge used is published or not, and if and how it is possible to obtain it.

Why unreliable: The method of acquiring external knowledge is not the focus of this paper.

**Example 8**
> Reviewer wrote: The metric called “precision@1” should be called “accuracy@1”

Why unreliable: The authors use precision as the evaluation metric for consistency of previous paper instead of accuracy.

**Example 9**
> Reviewer wrote: As far as I saw the Figure 2 and 3, the accuracy is heavily reflected by the amount data available during training and some normalization should be needed to compare these metrics each other without biases. Figure 3 also show some remarkable characteristics in translating only into C++, but the paper did not mention about this point.

Why unreliable: It is not that intuitive to compare the evaluation result to each other in Table 2 given the fact that they belong to different translation directions.

**Example 10**
> Reviewer wrote: These can happen in practice, but I'm not convinced flipping the label (essentially) is always beneficial especially in rare/infrequent classes settings.

Why unreliable: The proposed method did not "flip" the label in a hard assignment way, instead, they update the weight of soft assignment between the LF and label.

**Example 11**
> Reviewer wrote: The novelty of this work is mixed: the idea of using retrieval for in-context learning prompts is not new (this work cites Liu et al., 2022 and Rubin et al., 2022)..

Why unreliable: As claimed by the authors in the paper, this paper's main focus is the selective annotation, instead of the retrieval in-context learning. Therefore, this does not limit its novelty.

**Example 12**
> Reviewer wrote: I did not understand why the proposed method is restricted to the few-shot setting. Do gains go away in the full data setting?

Why unreliable: The authors already provide reasonable justification on this in their introduction section, i.e., assuming plenty of training data for every task is hard to acquire in most real scenarios as getting large labeled datasets is often expensive and time-consuming. The motivation of this paper is that humans can learn new tasks continuously even only see a few examples, and the authors wanted to build a model that can also do so.

**Example 13**
> Reviewer wrote: Besides, it seems that introducing a hyperparameter to balance  $L_\text{disc}$ and $L_\text{gen}$ is acceptable, as the author introduces such a hyperparameter in Eqn. 5 to balance the two loss term for finetuning, which is actually in a similar situation.

Why unreliable: These two are not similar. $L_\text{disc} + lambda * \L_\text{gen}$ is a mutli-task formulation, whereas Eqn.5 is learning with regularization because both terms in Eqn.5 optimize the same classification probability.

**Example 14**
> Reviewer wrote: Table 2: note that the bold-faced results are not the best for all columns.

Why unreliable: The bold-faced results are the best among methods that use text-only input.

**Example 15**
> Reviewer wrote: However, as the authors mentioned, this can be viewed as an external memory module and embedding lookup doesn't need much computation.

Why unreliable: The entity embeddings are parallel to the typical token embeddings thus viewing it as external memory poses additional computation cost. Whether this is a large or small factor in actual computation needs to be analyzed.

**Example 16**
> Reviewer wrote: Some parts about the proposed method are not clear, and there are a few missing and potentially misleading pieces in the paper.

Why unreliable: I think most unclear parts mentioned by this review are mostly from the reviewers misunderstanding.

**Example 17**
> Reviewer wrote: -- On the specific subset of SentEval tasks you’ve selected, the majority of the performance discrepancy is in the SICK-E task--otherwise, the overall #’s are rather interchangeable. How does this change if you add in the rest of the SentEval tasks, and why were they omitted? Analysis/exploration for why you get such a performance boost only on SICK-E would also be useful.

Why unreliable: Using the term "the majority of improvement" is not precise. And the majority of improvement does not only come from the SICK-E dataset.

**Example 18**
> Reviewer wrote: The scaling formula seems somewhat ad hoc and hard to characterize. In particular, if the sensitivity of some parameter spikes on a given iteration, it will get a larger update than another parameter with the same moving-average sensitivity that has not spiked.

Why unreliable: This paper has explained the reasons for the design of such a formula in Sections 1 and 3. Specifically, a large local temporal variation (“spike”) implies that there exists high uncertainty in the sensitivity. Therefore, the current sensitivity score is not yet a reliable indicator of redundancy. Accordingly, the paper suggests that we should avoid decreasing its learning rate no matter if the current sensitivity is large or small.

**Example 19**
> Reviewer wrote: However, this article only uses one dataset for pretraining, and does not use multiple datasets to test the required expert pool size.

Why unreliable: The dataset is a union of diverse datasets

**Example 20**
> Reviewer wrote: What will happen if we do not shuffle the sentences?

Why unreliable: If the sentences are not shuffled, then whole propose method and all its baselines cannot work.  This reviewer doesn't seem to get the basic context of these type of sentence-level loss functions. The authors also describled this in appendix C.

**Example 21**
> Reviewer wrote: You hypothesize that more templates doesn't help because "models at such scale do not easily overfit to a finetuning single task" - but my intuition is for an opposite explanation -- that the models at such scale easily memorize a small number of templates!

Why unreliable: This hypothesis was the authors' original motivation for writing ten templates per dataset. The results shown in the Appendix B ablations that this did not make a substantial difference in performance when there was a large number of tasks. This result certainly warrants further investigation, but it can somewhat support the authors hypothesize.

**Example 22**
> Reviewer wrote: However, the paper continues to be centered around the SentEval benchmark results. While SentEval is a useful benchmark to evaluate sentence representations, it doesn't reflect well how these representations will be used in practice.

Why unreliable: This paper is not only centered around the SenEval benchmark. The paper has a dedicated evaluation section for more realistic benchmark such as Amazon Reviews.

**Example 23**
> Reviewer wrote: Still, I believe the authors do not tackle a really important point, critical to assess the full potential of the methodology: how the knowledge distilled in the network vanishes, or not, as it is trained on more and more tasks.

Why unreliable: The authors perform recursive distillation to show that the vanishing knowledge is not much of a concern. However, more robust experiments could be performed.

**Example 24**
> Reviewer wrote: I don't recommend accepting the submission since the empirical results are well-known and the theorems don't provide theoretical justifications to the observations.

Why unreliable: This opinion is mainly due to the reviewer's misunderstanding of the paper. It requires more justification or references.

**Example 25**
> Reviewer wrote: Section 3 Proposed Method: curated -> created

Why unreliable: This shoudl not be a typo. The "curated" is appropriate in the context.

**Example 26**
> Reviewer wrote: Second, a common criticism of GLUE and other benchmarks which applies to FLEET is that the benchmarks (1) simply repackage and resell other datasets as a new benchmark without adding substantial new value and (2) contain a relatively ad-hoc selection of individual datasets. FLEET is similar in that it sort of throws together a collection of tasks (sentiment, NLI, etc.) mainly guided by low-level reasons (e.g., the class imbalances) rather than higher-level ones (e.g., based on practical few-shot scenarios, different types of reasoning, tests of spurious correlations, etc. ).

Why unreliable: These reviews minimize the paper contribution. Paper provides a detailed explanation of decisions for task selection.

**Example 27**
> Reviewer wrote: The proposed solution is to leverage data augmentation to generate task-specific unlabeled data.

Why unreliable: The paper does not leverage data augmentation to generate data; instead, the generated data can be considered as one type of data augmentation to improve performance. The proposed solution is to leverage generated data to improve the performance of knowledge distillation and few-shot learning.

**Example 28**
> Reviewer wrote: Similar studies were conducted on a single node with 8 GPUs as noted by the authors. Though that setup had considerably more computational resources the total volume of computation was still a fraction of the amount used by many large research institutions. In light of that work, the scenario presented in this paper may seem somewhat derivative and only marginally interesting.

Why unreliable: Similar prior work does not invalidate this study. The authors point to how their work is novel in this field.

**Example 29**
> Reviewer wrote: The claim that flatness can decide the downstream performance is not well-supported.

Why unreliable: Authors never claimed it. The authors only claimed that the pre-training validation loss does NOT decide the downstream performance.

**Example 30**
> Reviewer wrote: Due to lack of comparisons with relevant methods, I don’t think this paper has a high quality.

Why unreliable: No justification was provided for the mentioned point. The lack of comparison is an overstatement.

### Neglect

*The reviewer overlooks important details explicitly stated in the paper, resulting in unwarranted questions or critiques.*

**Example 1**
> Reviewer wrote: But all the tasks in your experiments are evaluated on high-level natural language understanding tasks, which typically require representations at higher layers.

Why unreliable: Figure 2 shows that the intermediate layer representation is effective on the QNLI and MRPC tasks.

**Example 2**
> Reviewer wrote: -It is not entirely clear how the shots are defined in the downstream tasks. Are they predefined in the scope of the datasets? This part can be more elaborated.

Why unreliable: The shots are already defined in Section 4. The reviwer overlooks it.

**Example 3**
> Reviewer wrote: It will be useful to see results for prompt tuning on other classification or QA tasks, for example from SuperGLUE, where the tasks require quite a different reasoning than LAMA.

Why unreliable: Similar results were indeed shown on three SuperGLUE tasks in Appendix B.

**Example 4**
> Reviewer wrote: Is it the performance for a given prompt? If so, that should be explained in the caption.

Why unreliable: Though the authors didn't mentioned the setting in caption, they did mention it in the paper.

**Example 5**
> Reviewer wrote: How could the findings benefit the community? The design principle of EncDec-based NMT is the sub-optimal performance/efficiency of LM-based NMT, and this paper just says: "yes, the intuition is true", which is not exciting at all.

Why unreliable: Authors point out that they conduted an analysis that was not done before and LMs are not always better than EncDec based NMT models

**Example 6**
> Reviewer wrote: Number of shots and classes: the numbers chosen here are a bit arbitrary and more concrete experiments could have been better.

Why unreliable: This is justified by the authors based on prior work as explanined in 4.3

**Example 7**
> Reviewer wrote: Usually, the bi-level formulations used in previous work present justifications of why such formulation is adopted, such as meta weight net, MAML, etc. However, no theoretical justification or intuitive explanation is given to explain the necessity and superiority of such a formulation in this paper.

Why unreliable: The paper provides intuitive motivation in Section 3.2 and Figure 2 for the usage of meta weight and bi-level optimization.

**Example 8**
> Reviewer wrote: It would be helpful if the author can show how much this will change the model's performance when the labels are correct.

Why unreliable: The authors show some results when the labels are correct in the third last paragraph of page 6 in the submission.

**Example 9**
> Reviewer wrote: The paper hints at the design of templates for the UniFew baseline but does not provide enough details for replication.

Why unreliable: Details about Unifew, including the exact prompt templates used for each task are already included in the appendices C and D (this is mentioned in lines 280-281 in the paper). The author also have included source code to facilitate replication. The reviewer overlooked them.

**Example 10**
> Reviewer wrote: In other words, the authors further need to whether the improvements over CB (in Table mainly come from by keeping or perfectly memorizing the corpus used for pretraining CB, or whether it comes from the use of new but well-matched corpus that is NOT seen when pretraining CB.

Why unreliable: This manuscript discusses it in section 5.5.

**Example 11**
> Reviewer wrote: There is a lack of in-depth observation on how to combine different answers; (2) different answers are obtained by controlling the temperature and k. For text generation, the effect of these two hyperparameters is unclear. In particular, how these two hyperparameters affect answer consistency is unclear.

Why unreliable: The authors showed the effect of different temparutre and k in Figure 4.

**Example 12**
> Reviewer wrote: In the multi-hop setting, do the numbered prompts like "Recitation 1" and "Recitation 2" naturally give rise to generating recitations of different topics, or does one have to train/update the LM to solicit such behaviour?

Why unreliable: The authors report multi-hop results with few-shot in-context learning, so the LM is pre-trained and does not need to be updated. Empirically, "Recitation 1" and "Recitation 2" do tend to generate different (or complementary) topics, as shown in Figure 13

**Example 13**
> Reviewer wrote: Is the dataset and CoT explanation publicly available?

Why unreliable: The authors metioned in the Abstract that the dataset is available.

**Example 14**
> Reviewer wrote: How many times did you run the experiments for each task and calculate the averaged performance? Since the improvements for many tasks are marginal and the variances looks not low enough. It would be better if you conduct a statistical significant test.

Why unreliable: The authors mention in checklist that their experiments are run three times, which the reviewer seems to have overlooked.

**Example 15**
> Reviewer wrote: After the selection of instruction using different metrics, a set of final instruction are returned, how do these extraction are used? prompted all of them in an in-context learning scenario?

Why unreliable: The authors described this question in Section 3: "... ultimately choosing the instruction with the highest score."

**Example 16**
> Reviewer wrote: The proposed method is pretty limited to the classification tasks, particularly for news classification, where the label names are informative and have many semantic relevant words in the vocabulary.

Why unreliable: The authors show improvement in other tasks as well

**Example 17**
> Reviewer wrote: Paper lacks any results about biases based on religion and race even though they claim to have done so in the initial section of the paper.

Why unreliable: Results related to religion and race exist in the appendix

**Example 18**
> Reviewer wrote: The prompt based UniFew baseline also seems both simple and effective, although I would like to see more details of the prompt template design in the main paper.

Why unreliable: Details about Unifew, including the exact prompt templates used for each task are already included in the appendices C and D (this is mentioned in lines 280-281 in the paper). The author also have included source code to facilitate replication. The reviewer overlooked them.

**Example 19**
> Reviewer wrote: The presentation and the writing of the paper can be further improved with more illustrative examples and case studies for readers to qualitatively see the problem setup and the differences between these methods.

Why unreliable: The authors provided illustrative examples of the CKL benchmark in Table 6 in Appendix B.3 Dataset Statistics and Examples.

**Example 20**
> Reviewer wrote: I think the analysis of model size is quite helpful, since a natural question is whether or not these results are due to the ELECTRA small model being too small to benefit from pre-training on massive upstream datasets.

Why unreliable: In the paper, the authors conducted experiments on a larger model - Roberta-base.

**Example 21**
> Reviewer wrote: Particularly, when is bootstrapping+self-amplification+ensembling are used? Is it used only during translation?

Why unreliable: The author has already clarified it in the appendix.

**Example 22**
> Reviewer wrote: I remain skeptical about the performance gain of the proposed method. Firstly, the authors do not compare with the important baseline that directly uses few shots in the demonstration(as in-context examples) to generate augmentation data, and then use the labeled few shots and synthetic data to fine-tune a PLM classifier.

Why unreliable: The GPT3Mix baseline mentioned in Section 5.1 is exactly a few-shot demonstration method for augmentation, and it uses a much larger generator (175B GPT3). The reviewer overlooks it.

**Example 23**
> Reviewer wrote: Is the finetuned BERT-Large a few-shot finetuned or with the full dataset?

Why unreliable: In section 4.2, the authors state that BERT-large is few-shot finetuned.

**Example 24**
> Reviewer wrote: Furthermore the EB-C metric is basically proposed from thin air.

Why unreliable: This is not true. The authors introduce the concept in the prior sections.

**Example 25**
> Reviewer wrote: Other collection sources for retrieval such as Wikipedia or the training corpus of Gopher 280B also need to be used for evaluation, in addition to Google’s results on internet.

Why unreliable: This manuscript also reports the results using Wikipedia-based DPR in the appendix.

**Example 26**
> Reviewer wrote: I feel like the authors didn't convey an incentive for this.

Why unreliable: The authors give a motivation for the analysis.

**Example 27**
> Reviewer wrote: It seems like the optimal value of k in vote-k would depend on the number of instances in the unlabeled set that changes with the tasks. A single value of k=150 was chosen for experiments across all tasks. Could the authors justify this choice further?

Why unreliable: In Section 2.1, underder the Vote-k methods, the authors explalin the reason why they set k=150: they did preliminary experiments and found that k=150 performs well across many datasets. Therefore, I don't think it is neccessary to find the most optimal k values for each task.

**Example 28**
> Reviewer wrote: It is also limited when the label names are multi-word expressions or phrases.

Why unreliable: The authors have talked about this case in the paper

**Example 29**
> Reviewer wrote: For example, what is the Transfomer stack used by Charformer? It seems like T5, but I don't find it mentioned anywhere.

Why unreliable: The Transfomer stack has been described in Section 2.2.

**Example 30**
> Reviewer wrote: It would be better if authors can add some insight or feature-based analysis on the emergent ability of cross-lingual reasoning of the tested language models GPT-3 and LLM.

Why unreliable: Author showed experiments in Figure 4 of the paper.

### Vague Critique

*The review lacks specificity, claiming missing components without clearly identifying what is missing.*

**Example 1**
> Reviewer wrote: The root cause of this is that the paper did not provide a reasonable criterion about acceptance of this experiment first.

Why unreliable: This is a vague critique and does not provide details.

**Example 2**
> Reviewer wrote: The experiment section is weak.

Why unreliable: Very subjective and vauge. The reviewer should provide explanations.

**Example 3**
> Reviewer wrote: This paper while taking a step in the right direction, seems a little premature for publication. That being said, the reported results my be of some value after all. It is hard to narrow down on the exact contributions of this paper.

Why unreliable: The reviewer seems to not provide many concrete ideas on this paper but subjectively says this paper is "premature for publication".

**Example 4**
> Reviewer wrote: _ "Our leading hypothesis here is that the LSTMs may actually relearn all weights without taking advantage of pretraining".

Why unreliable: The reviewer has forgotten to indicate the issue with this sentence from the paper

**Example 5**
> Reviewer wrote: The setting of using a shorter explanation becomes out of the general hypothesis. This might become a strength if it were presented as a limitation and not as a solution.

Why unreliable: This statement is vague and difficult to understand. The reviewer should provide reasons why to make this statement.

**Example 6**
> Reviewer wrote: some grammatical mistakes and typos.

Why unreliable: The reviewer should provide examples to illustrate the grammatical mistakes and typos.

**Example 7**
> Reviewer wrote: Individual problematic ingredients are neither being theoretically-proven nor empirically-proven.

Why unreliable: This is a vague and unreliable comment. The review does not specify what the "problematic ingredients" are. The experiments mentioned in this paper are all empirical analysis.

**Example 8**
> Reviewer wrote: The new findings are not particularly non-trivial.

Why unreliable: There is not enough justification provided by the reviewer for this claim.

**Example 9**
> Reviewer wrote: But the novelty of the proposed method is weak.

Why unreliable: It is unfair to claim weak novelty without offering much justification.

**Example 10**
> Reviewer wrote: I believe regardless of how good some of transfer learning models perform, we need to elaborate on situations those models collapse.

Why unreliable: It is not clear why the elaboration on model collapsing is needed

**Example 11**
> Reviewer wrote: I wonder if the proposed method is necessary.

Why unreliable: This comment is vague and thus needs further explanation.

**Example 12**
> Reviewer wrote: Improvements over the baselines are not fully convincing.

Why unreliable: This is a vague critique. The reviewer made this critqiue without enough justification.

**Example 13**
> Reviewer wrote: clear presentation, but not very original

Why unreliable: This opinion requires more justification or references.

**Example 14**
> Reviewer wrote: 1. The data contribution seems small and somewhat unnatural. The hypothesis format seems extremely unnatural (being text referential). I wonder if such examples are out of domain for the trained NLI systems.

Why unreliable: There is no reasoning or explanation for this statement. Subjective terms such as unnatural need more backing when used to explain a work.

**Example 15**
> Reviewer wrote: There is inconsistency in presentation.

Why unreliable: The review does not provide where is the inconsistency.

**Example 16**
> Reviewer wrote: Technical details are missing/not clearly described. Experimental results are sparse and not fully convincing.

Why unreliable: This review is vague and lacks reasons and validity. There is no explanation providing context to the statements.

**Example 17**
> Reviewer wrote: I would suggest comparing them all together to support validity of the scrambling methods.

Why unreliable: It is not clear what is meant by 'compare them all together'. If this is relevant to adversarial attacks, then it is out of scope

**Example 18**
> Reviewer wrote: The main issue of the paper is the novelty of the proposed method. Based on technical novelty and insufficient experiments, I don’t think the current version meets the standard of the ICLR.

Why unreliable: The reviewer made this conclusion without enough support evidences. The authors have done enough experiments and show novelty.

**Example 19**
> Reviewer wrote: The novelty contribution is somehow limited.

Why unreliable: This is lazy review point to mention without context. As mentioned in the Related Works section of the paper, the objective of using contextualized embeddings in kNN-LM and CGR is different. CGR is the first work to entirely replace the decoder vocab space from model vocab embeddings with contextualized embedding space from the training step.

**Example 20**
> Reviewer wrote: One potential shortcoming of the work is that its technical contribution may not be sufficient for a research paper.

Why unreliable: The reviewer did not provide any evidence to support this claim.

**Example 21**
> Reviewer wrote: Testing all five is very inefficient.

Why unreliable: The review does not provide why testing all five is inefficient.

**Example 22**
> Reviewer wrote: The solution of calling another model contradicts slightly a comment about "external tools" right before the subsection "Contributions" on page 2.

Why unreliable: Could have elaborated better.

**Example 23**
> Reviewer wrote: Lots of experimental results that are not well explained

Why unreliable: This is a vague critique. The reviewer should provide what results that are not well explained.

**Example 24**
> Reviewer wrote: -- “after exploring options including [CLS] representations and max pooling.” what was the performance drop?

Why unreliable: This is an unclear and confusing question.

**Example 25**
> Reviewer wrote: However, I notice usually a dense model (350M) could get a score of 70.2 on piqa.

Why unreliable: The reviewer did not indicate which dense model was used

**Example 26**
> Reviewer wrote: The technical novelty of this paper is a little limit. The total contributions are also limit.

Why unreliable: A general statement that is neither constructive nor refutable

**Example 27**
> Reviewer wrote: There is some part quite hard to follow.

Why unreliable: The description is too vague.

**Example 28**
> Reviewer wrote: Weaknesses: Some important details are missing.

Why unreliable: The reviewer should explain what important details are missing instead of making such a general critique. This is a vague critique.

**Example 29**
> Reviewer wrote: Analysis on generated explanation is also weak.

Why unreliable: Not substantiated by explanation

**Example 30**
> Reviewer wrote: (Con) Many technical details are unclear/confusing.

Why unreliable: There is no explanation of what content is unclear or confusing.

### Out-of-scope

*The reviewer suggests additional methods, experiments, or analyses that are beyond the intended scope of the paper.*

**Example 1**
> Reviewer wrote: Recently, the Chain-of-Thought prompting (https://arxiv.org/pdf/2201.11903.pdf) has been used by many papers using in-context learning, with reported improvements in model performance (the paper seems to have been cited already 100 times since its release earlier this year). One question this work does not address is whether model sensitivity/variance to retrieved prompts is also present when used in conjunction with chain-of-thought. And whether the vote-k scheme would be useful to limit the number of chain-of-thought annotations needed to improve in-context learning performance.

Why unreliable: This is a out-of-scope topic for this paper since the experiments are sufficient enough for general in-context learning. This could be a future work.

**Example 2**
> Reviewer wrote: Lastly, a final concern about real-world utility as the prompting does not perform well on harder problems (logical tasks).

Why unreliable: This is out of scope for the paper

**Example 3**
> Reviewer wrote: How does the pre-training (i.e., datasets, model design) of LLMs affect their multilingual abilities?

Why unreliable: The paper does not involve the pre-training of LLMs. I think this questions is out of the scope of this paper.

**Example 4**
> Reviewer wrote: The demonstrated examples are all for very basic arithmetic operations, and it is unclear whether this technique can scale to more complicated cases.

Why unreliable: out of scope for the paper

**Example 5**
> Reviewer wrote: What is the complexity (time and space) of weak supervision?

Why unreliable: The "time and space"complexity of weak supervision should not be a problem in the scope of this paper.

**Example 6**
> Reviewer wrote: It is not clear if and how the approach extends to other types of knowledge, outside of the e-commerce and products domain.

Why unreliable: This is not the focus of this paper

**Example 7**
> Reviewer wrote: (~) MTPB does not allow for "going back" (i.e., a user indicating that a generated response is wrong & clarifying their prompt).

Why unreliable: This paper focuses on factorizing a complex problem to simple subproblems, the "going back" is out of scope

**Example 8**
> Reviewer wrote: A more systematic analysis is needed to determine the optimal prompts that make the model capture a range of different patterns. This sentence seems to indicate that this will be the focus of the paper, but it isn't my understanding of the purpose of the paper.

Why unreliable: The reviewer's suggestion is off topic and is out of the scope of this paper.

**Example 9**
> Reviewer wrote: Since this is an examination work on multiple translation models and configurations, it would have been nice to provide a deeper analysis on the linguistic aspects of the experiments as well: Language pairs with different characteristics (morphologically rich languages for instance) work differently with different models. How different variations of the same model perform on different classes of languages is a significant question to investigate.

Why unreliable: Already paper has many experiments. Adding this would be out of scope

**Example 10**
> Reviewer wrote: In fact, this proposed method could be applied in sequence-to-sequence pretraining model, such as mT5. Have you explored this direction? Or leveraging synthetic parallel data generated by the GPT-3 to warm up the previous UNMT models?

Why unreliable: Out-of-scope. The main focus of this paper is decoder-only LMs.

**Example 11**
> Reviewer wrote: The current draft does not address impacts of less-accurate or incorrect recitations.

Why unreliable: This problem is a common issue of the Chain-based method --- there could be a lot of hallucination chains generated by the models, which is a big issue in this area and is beyond the contribution of this paper.

**Example 12**
> Reviewer wrote: Given the workarounds for dealing with the max amount of tokens, I'd like to see a reflection on the potential limitations of LLM reasoning.

Why unreliable: Limitations related to LLM reasoning have been discussed at length in past research

**Example 13**
> Reviewer wrote: Would a user be able to specify the sub-tasks in the required format (such as defining appropriate variables) as in Figure 1?

Why unreliable: Many problems in benchmark express the specification at high-level, and one does not have to specify in a right way

**Example 14**
> Reviewer wrote: Representations from the encoders are held fixed and linear classifiers are trained on top of these fixed representations on downstream tasks using labelled data. To me, this is not a setting that demands sentence vectors. It only shows that the sentence vectors capture useful features. I would suggest focusing on a setting where the advantage of the sentence vectors can be demonstrated such as a retrieval problem.

Why unreliable: This argument is orthogonal to the paper topic.

**Example 15**
> Reviewer wrote: (2) can you compare the proposed method with some soft prompt tuning method?

Why unreliable: Out-of-scope, this paper mainly focuses on selective annotation for reducing labeling costs as opposed to finding/tuning better prompts

**Example 16**
> Reviewer wrote: It is unclear to what extent the tasks + evaluation protocol considered here are reflective of language understanding.

Why unreliable: This question is too broad for this paper to answer.

**Example 17**
> Reviewer wrote: Another concern is the efficiency at inference time.

Why unreliable: Time efficiency is not an objective of this work

**Example 18**
> Reviewer wrote: They could evaluate on sentence embedding and probing tasks (like SentEval) and see how the two models compare. It would be interesting to see wha encoded information differs between the models.

Why unreliable: Evaluating the embedding differences on SentEval is out of the scope for this paper.  Some NLI-related tasks in SentEval is already covered in this paper. Evaluating on other tasks that are not directly related to NLI has little point to show since, as the title claimed, this paper is about entailment-based sentence embeddings.

**Example 19**
> Reviewer wrote: Can we improve the results by simply increasing k?

Why unreliable: I think this is another important research question, that investigates the number of demonstrations in context, which goes beyond this paper's responsibility.

**Example 20**
> Reviewer wrote: More content on how this can be expanded to multilingual settings and other task types would be useful.

Why unreliable: This could be a future work and it is out-of-scope for this paper. Therefore it is not a valid criticism

**Example 21**
> Reviewer wrote: In particular, good directions can include in-the-wild performance when tested on something outside of coding-problem data sets (especially since those are so well-organized by language and problem).

Why unreliable: The main focus of this work is mining parallel datasets for learning code translation models. The requirement of testing the method on something outside of coding-problem datasets is a little out-of-scope.

**Example 22**
> Reviewer wrote: Some examples: Can algorithmic prompting be extended to operations we only know the structure of? Like solving dynamic programming problems with demonstrations for a DP problem with different state space or update functions?

Why unreliable: out of scope for the paper

**Example 23**
> Reviewer wrote: Besides the LM task, it could be better if more document-level downstream tasks could be evaluated to verify the usefulness of the proposed approach.

Why unreliable: The paper demonstrates improvements across several datasets using language modelling, which is acutall already a diverse task, rather than focusing on downstream tasks.

**Example 24**
> Reviewer wrote: Furthermore, the paper topic is too narrow, it would be much better to extend to other language generations tasks, like dialogue and QA (not a weakness but a suggestion).

Why unreliable: The authors do a deeper analysis in this narrow field and this is also a meaningful contribution.

**Example 25**
> Reviewer wrote: It will be more inspiring if the authors can give some high-level principles. Is it possible to design a more general framework that can work well when shifting to a new domain?

Why unreliable: This is not the focus of this paper

**Example 26**
> Reviewer wrote: My main concern is that I'm not sure this is enough for a full paper. This is a useful analysis and prompt engineering strategy, but I would expect either a deeper analysis of why formulating things as Q/A works so much better (e.g., analysis of the training data), or

Why unreliable: Personally, I think "investigating the reason why Q/A prompting can work well" is too hard to conduct, which is somehow beyond this paper's scope. To my knowledge, there are several pieces of literature actually do this and can be regarded as "full paper" as well.

**Example 27**
> Reviewer wrote: Evaluation protocol: It is unclear if the evaluation protocol considered is measuring language understanding capability well.

Why unreliable: This question is too broad for this paper to answer.

**Example 28**
> Reviewer wrote: (-) MTPB (from a cursory qualitative evaluation of examples) seems to rely on very fine-grained prompts. In many examples in App F, the prompts are substantially longer than the required code.

Why unreliable: Beyond the scope of the current work

**Example 29**
> Reviewer wrote: The method is applicable to mT5 style models, but the long-term solution is probably to adapt mT5 models with causal LM or prefix LM objectives.

Why unreliable: This is an orthogonal point (a new direction), which is out-of-scope for this paper.

**Example 30**
> Reviewer wrote: It may be good to expand the scope of the paper to generation tasks, as these are likely more suceptible to adversarial attacks. What I mean by this is that the worse case scenario is much worse for generation tasks: while in binary classification the worse case is bad accuracy, for adversarial attacks on generation tasks, potentially very harmful text could be generated, which is much worse than simply getting the answer wrong.

Why unreliable: Generation tasks would be a completely different setting and not in the scope of the paper

### Invalid Criticism

*The reviewer's criticism is considered invalid, especially when suggesting impractical experiments or trivializing results.*

**Example 1**
> Reviewer wrote: Based on my inference, the approach is reasonable but not terribly surprising.

Why unreliable: This statement is too subjective. The claim of "the apporach is not supprising" should not be a resasonable weakness of a paper.

**Example 2**
> Reviewer wrote: Results are not particularly surprising

Why unreliable: This is a invalid criticism. Many findings seem obvious in retrospect, but this does not mean that the community is already aware of them and can use them as building blocks for future work.

**Example 3**
> Reviewer wrote: Besides, the empirical observation and proposed fine-tuning method are pretty straightforward and not surprising.

Why unreliable: The straightforward of the method should not be a weakness. Additionally, it is not contructive to say the results are not suprising. Not suprising does not mean that other researchers are already aware of them.

**Example 4**
> Reviewer wrote: Another concern is that the contribution of this paper to research community may be weak, if the code is not released and the results are not easily reproduced.

Why unreliable: Just because the code is not public does not mean that the reproducibility of this paper is not good.

**Example 5**
> Reviewer wrote: -- SentBERT → SentenceBERT or SBERT

Why unreliable: This is an overly harsh typo inspection.

**Example 6**
> Reviewer wrote: The proposed method (objectives) is hard to transfer to other domains.

Why unreliable: Most pre-trained objectives that incorporate domain knowledge have such problems. However, it is still a meaningful research for a specific domain.

**Example 7**
> Reviewer wrote: More importantly, it requires highly-structured and large-scale in-domain data for pretraining, which might not be available in other domains.

Why unreliable: Perhaps there are other domains where there is a large amount of highly structured data. For example, data in the financial domain contains information about stock prices, stock reviews and other information.

**Example 8**
> Reviewer wrote: I would like to see the empirical results on stronger models, like RoBERTa related models.

Why unreliable: This is an example of a weak review provided by ACL It is not weak to have all the baselines not covered in the paper.

**Example 9**
> Reviewer wrote: There are models that accept more tokens, and some that claim to accept an unbound number (I expect them to deteriorate).

Why unreliable: But still token limitation is a problem with the free models available at that time.

**Example 10**
> Reviewer wrote: Furthermore, while several baselines were provided, there have been many architectures recently proposed, and probably more comparisons are needed to fully justify the method.

Why unreliable: Since there are many models coming out on each day, comparing with all of them do not seem to be realistic. The paper provides a good coverage of popular models in its first submission.

**Example 11**
> Reviewer wrote: A proper analysis would consider more heldout tasks and permutations of training data, but presumably this is prohibitively expensive.

Why unreliable: This segment should serve more as a question than as a weakness, because the reviewer already points out that this suggestion is unrealistic due to expensive training cost. So this segment does not count as a weakness against this paper.

**Example 12**
> Reviewer wrote: So, in its current form this does not enable any new abilities as we could use the base algorithm instead of using expensive LMs.

Why unreliable: The comment is too general and not relevant to the main research problem in this paper.

**Example 13**
> Reviewer wrote: 17- Section 7: the author mentions a key difference between T0 and FLAN model is that T0 is an encoder-decoder model which is pretrained and finetuned with different objectives. However, no clear comparison with FLAN model is presented in the paper

Why unreliable: Flan is a concurrent work, the author of this paper doesn't have the duty to compare T0 with the FLAN.

**Example 14**
> Reviewer wrote: While it's good to quantify the performance of models on time-stratified datasets, many conclusions are obvious, such as the synthetic experiments on question answering by shifting the end year of training data, as well as the experiments on self-containing reading comprehension.

Why unreliable: The "conclusions are obvious" shouldn't be the weakness.

**Example 15**
> Reviewer wrote: The way to add structural locality is straightforward.

Why unreliable: Straightforward is not a bad thing

**Example 16**
> Reviewer wrote: Another concern regarding the paper that I have is that most of the results are pretty well-known - e.g. performance of open-book models are better than parametric models, and Google search is better.

Why unreliable: "the results are well-known" should not be the reason for rejection. The experiments of this paper are simply to demonstrate the performance superiority of the internet-augmented method, instead of "demonstrating any conclusion".

**Example 17**
> Reviewer wrote: The paper misses fair comparisons with many significant related work including autoregressive sparse MoE, GLaM [1].

Why unreliable: The suggested work for comparison, GLaM, has been cited and discussed in related work. The GLaM code and dataset are not publicly available, so the authors cannot make a direct comparison. Furthermore, this paper indeed compared SaMoE with two other state-of-the-art open-sourced MoEs from DeepSpeed-MoE, which include an autoregressive sparse MoE (denoted as AR-MoE) and a parameter-efficient MoE (denoted as PR-MoE) trained on the publicly accessible dataset PILE.

**Example 18**
> Reviewer wrote: Various efficient routing functions should be compared with in this work, as intelligent routing functions achieve similar effects of improving parameter efficiency.

Why unreliable: Expert sharing and routing are orthogonal ideas

**Example 19**
> Reviewer wrote: Representational similarity For beginners, the word of representation similarity is not easy to follow. At least, authors should define the terminology in the introduction.

Why unreliable: Not a valid concern. While the authors do not provide a formal definition, similarity detection is a well-established sub-field and the authors provide valid citations.

### Superficial Review

*The reviewer appears to have only skimmed the paper, providing generic or unsupported comments about the presence or absence of weaknesses.*

**Example 1**
> Reviewer wrote: Does it hurts the model in a way that we don’t know yet? What type of hallucination in language generation when the model is trained on diverse datasets?

Why unreliable: The question is too general and can challenge almost any manuscript on the related topic.

**Example 2**
> Reviewer wrote: Quality and Significance: Overall, this is a good application method and might be useful for many practical applications.

Why unreliable: Need more detail for this claim. There is very little context to the statement making it not very reliable.

**Example 3**
> Reviewer wrote: The Experiments are extensive.

Why unreliable: This statement is an opinion with no justification. There needs to be a valid justification for pointing out the strengths and weaknesses of the paper reviewed.

**Example 4**
> Reviewer wrote: Strength: This paper is well written and easy to understand.

Why unreliable: Again, just a line for estimating the strengths of a paper is poor reviewing. The reviewer could have placed more attention and effort in writing this section.

**Example 5**
> Reviewer wrote: Compared to the FCM in this paper, I think the performance of causal masking methods from [2] might be better.

Why unreliable: This claim is not backed by evidence

**Example 6**
> Reviewer wrote: The authors did mention one ablation in the supplementary that I missed, but I don’t think that is sufficient for a reader to understand how to build on this method in this future without re-running all the experiments, doing an extensive hyperparam search, etc.

Why unreliable: This comment is too general. Most papers have this limitation.

**Example 7**
> Reviewer wrote: The empirical results are solid and strong.

Why unreliable: The experiments are kind of limited in a narrow domain for the proposed general method. Thus, it is difficult to say results are solid and strong.

**Example 8**
> Reviewer wrote: Designing metrics for exposure bias is a novel task, and this paper invented appropriate approaches.

Why unreliable: This work is not demonstrated to be novel and the statement is too brief to explain the novelty of the work.

**Example 9**
> Reviewer wrote: This paper proposes a new few-shot learning method for NLP problems by incorporating a simple,effective framework.

Why unreliable: The summary is too general and not specific to the main focus of this paper.

**Example 10**
> Reviewer wrote: This paper provides a simple, yet effective approach to the few-shot learning problem.

Why unreliable: The summary is too general and not specific to the main focus of this paper.

**Example 11**
> Reviewer wrote: Quality: This paper is of high quality, the empirical evidence provided is very strong, the logical flow of the experiments and presentation is coherent and consistent.

Why unreliable: This review is too general and can apply to any current deep learning paper. It does not give any specific insights on this paper.
Besides, the generalizability of this analysis is problematic.

**Example 12**
> Reviewer wrote: The results that authors demonstrate are very compelling and reliable. The analysis on the token and sentence level embedding is insightful.

Why unreliable: The reviewer should provide more detailed points to support this statement

**Example 13**
> Reviewer wrote: The proposed continual knowledge learning problem is quite interesting and important.

Why unreliable: This statement is quite vague even though it is a strength. It does not provide enough context to other reviewers or the AC as to the paper's exact strengths.

**Example 14**
> Reviewer wrote: The FUAR metric is also technically sound.

Why unreliable: This statement is very vague and not reliable as there are no supporting evidence for the claim.

**Example 15**
> Reviewer wrote: The proposed continual knowledge learning problem is quite interesting and important. The benchmark is useful and the proposed FUAR metric is technically sound.

Why unreliable: Repetitive comments without any description of the comments made. The reviewer already mentions the same before and in both cases provides no supporting evidence for the claim.

**Example 16**
> Reviewer wrote: The paper is technically sound.

Why unreliable: Vague comment with no details to the claim made.

**Example 17**
> Reviewer wrote: We can find more in the paper.

Why unreliable: This is a very superficial statement.

**Example 18**
> Reviewer wrote: The paper doesn't have too many weaknesses.

Why unreliable: This statement is superficial and indicates that the reviewer might not spend enough time checking the details of this paper.

### Unstated statement

*Statements made in the review are not supported by content in the paper.*

**Example 1**
> Reviewer wrote: Ease of use, being conceivably language agnostic, training more efficiently and allowing easy reimplementation (pytorch), make this work a welcome contribution to the field.

Why unreliable: This paper did not upload the code when it was submitted, and the conclusion of this review cannot be verified.

**Example 2**
> Reviewer wrote: Like previous work, they perform multitask prompted fine-tuning on 40+ NLP tasks but while retrieving from external knowledge sources to perform the task.

Why unreliable: There is no (multitask prompted) fine-tuning on 40+ NLP tasks in this paper

### Excessive demands

*if the weaknesses are just asking for excessive things that are not necessary for a good paper.*

_No examples available in the source dataset._

### Generic comment

*weaknesses are just generic comments that can apply to any paper, without really pointing out the specific problems of the paper.*

_No examples available in the source dataset._
