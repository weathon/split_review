# Rethinking Mixture-of-Agents: Is Mixing Different Large Language Models Beneficial?

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 6, 3

## Abstract
Ensembling outputs from diverse sources is a straightforward yet effective approach to boost performance. Mixture-of-Agents (MoA) is one such popular ensemble method that aggregates outputs from multiple *different* Large Language Models (LLMs). This paper raises the question in the context of language models: is mixing different LLMs truly beneficial?  We propose Self-MoA --- an ensemble method that aggregates outputs from only the *single* top-performing LLM. Our extensive experiments reveal that, surprisingly, Self-MoA outperforms standard MoA that mixes different LLMs in a large number of scenarios: Self-MoA achieves $6.6\%$ improvement over MoA on the AlpacaEval 2.0 benchmark, and an average of $3.8\%$ improvement across various benchmarks, including MMLU, CRUX, and MATH. Applying Self-MoA to one of the top-ranking models in AlpacaEval 2.0 directly achieves the new state-of-the-art performance ranking $1^{\text{st}}$ on the leaderboard. To understand the effectiveness of Self-MoA, we systematically investigate the trade-off between diversity and quality of outputs under various MoA settings. We confirm that the MoA performance is rather sensitive to the quality, and mixing different LLMs often lowers the average quality of the models. To complement the study, we identify the scenarios where mixing different LLMs could be helpful. This paper further introduces a sequential version of self-MoA, that is capable of aggregating a large number of LLM outputs on-the-fly over multiple rounds, and is as effective as aggregating all outputs at once.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a revision to the Mixture-of-Agents approach, which first samples responses from multiple diverse LLMs / agents (proposers), before feeding it into a final LLM (an aggregator) to generate a final response given the other LLM's responses. The paper argues that the prioritization of diversity of proposer LLMs in the response generation phase increases the utilization of low quality models, thereby hurting overall MoA quality.

The paper then proposes Self-MoA: instead of sampling k total proposals from n different LLMs, one can sample k proposals from the best overall LLM. By doing so, Self-MoA outperforms standard MoA on the same model settings and benchmarks. When applied to SoTA open source models on AlpacaEval 2.0 leaderboard, Self-MoA achieves SoTA, setting a new high score in the public leaderboard. To motivate their change, the paper performs an empirical study of the trade-off between proposal quality, proposal diversity, and end MoA quality, in a controlled setting. The study is evaluated on MMLU, CRUX (Code), and MATH, considering proposals from models that are experts in each respectively. The paper finds that while both proposal quality and diversity correlate with end quality, there is a trade-off between them, and the strongest end-MoA quality results prioritize quality. Thereby motivating their method.

Finally the paper introduces a variant of Self-MoA , called Self-MoA-Seq, that allows for unconstrained MoA scaling w.r.t. the aggregator model's context-length. It does this by breaking up the large number of proposals over multiple rounds of aggregation. They find that Self-MoA-Seq maintains or improves upon the quality of Self-MoA, without requiring as long as a context length. They however, do not find that Self-MoA responses necessarily get better with increased sampling scaling.

### Strengths
Originality & Significance:
- This paper is the first to thoroughly study the trade-off between the quality and diversity of proposer LLMs in the Mixture-of-Agents framework. Importantly, by doing this analysis, they find that the existing MoA approach may overemphasize diversity, regardless of proposer quality, and in fact low proposer quality can negatively impact end MoA quality. (Among other interesting findings.)
- They propose an effective revision to MoA: use only the best agent but sample multiple diverse responses (up to the same sampling budget as MoA). They demonstrate that on a major leaderboard like AlpacaEval 2.0 this variant outperforms standard MoA and sets a new record / all time SoTA result. This is a very significant result. 
- Generally this finding would be important to the community, to highlight the possible pitfalls of doing MoA, and serve as a deep dive into the specific design decisions to consider when applying such an approach. 

Quality:
- The paper presents a thorough study of the tradeoffs between different compositions of proposing agents in the MoA process. 
- The methodology is well controlled to be directly comparable with MoA, and the baselines are strong. 

Clarity: The paper is clearly written and laid out. It is easy to read and follow, free of writing or grammatical errors.

### Weaknesses
1. Soundness. I have major soundness concerns regarding how the authors interpret the results of their experiments. Regarding Table 3, on lines 261 to 265, the authors write that only two configurations (of proposer compositions) of MoA slightly outperform / match Self-MoA, with the rest underperforming Self-MoA. However, the authors here take the overall average at face value for this comparison.
- When looking at this "best Self-MoA" configuration, "dddddd", this configuration is the worst on MMLU, and in the bottom half for MATH. The overall average of this method only beats the others since it appears that CRUX (Coding) shows the most variance in scores from MoA configurations. Allocating all samples to 'd' improves coding the most, and the outlier coding result boosts the overall average of Self-MoA. 
- The basic MoA, that allocates sampling budget equally across agents "iiddmm" beats Self-MoA "dddddd" on 2 of 3 capabilities. 
- The best results in the table are the TaskBest results. However it is unclear to me how TaskBest is "Self-MoA" rather than "Mixed MoA" as it still uses a mixture of all the agents.

In the end, the paper asks the overarching question "Is mixing different large language models beneficial?" and the paper's Table 3 essentially does show: yes it is, although the authors do not acknowledge this. The value of MoA lies in the ability to potentially construct a well rounded model from multiple different experts. In Table 3 every row that uses multiple models have a better capability balance than the author's proposed single-model method "dddddd", which excels only in Code and uses this narrow ability to bolster the overall average. TaskBest results here directly disproves the single-model Self-MoA proposal of the paper, showing that the best overall results come from deciding when to use each of the expert models. 

2. Soundness. A counter argument to my concern above might be Table 2, where the authors are able to boost a single general model to #1 on AlpacaEval 2.0. While this is true, AlpacaEval represents a specific evaluation setting and does not necessarily imply that there is no value to mixing multiple models. This #1 result also uses a stronger base model that was not tried by the original MoA method. This result then, while impressive, does not provide insight on whether Self-MoA is better than Mixed-MoA.
- In Table 1, a more fair comparison is done. While Self-MoA improves over 3-layer MoA by 0.3 win rate, this small amount is certainly within the margin of noise for win rate for any autorater. The original MoA paper reports the noise for the eval to be +/- 0.6. It is fair to say however that Self-MoA is able to save some compute in the process.
- I will also note that in Table 1, the use of "forward pass" is incorrect as decoding a generation requires multiple forward passes. The authors seem to mean just the number of proposals / generations required. 

Overall for the authors to be able to claim that Self-MoA is better than Mixed-MoA in terms of end-quality on challenging real benchmarks, the authors would need a fair comparison, and to show a larger margin of gain given the autorater noise. This comparison would benefit from using a second benchmark also other than AlpacaEval 2.0. Such as MTBench, as shown in the original MoA paper.  
It would also be important to show that the benchmark hacking raised in (1) doesn't happen for AlpacaEval 2.0 / MTBench -- that the method improves on similar prompt categories as Mixed-MoA and does not overfit to one particular category. 

4. Presentation: 
- Section 4 feels a bit out of place for the paper. Solving the ability to scale MoA to arbitrary number of samples seems to be a different problem altogether. It is unclear why the Self-MoA-Seq technique couldn't be applied to Mixed-MoA, and where there isn't a comparison with Mixed-MoA in the inference scaling experiment. In this setting I would expect Mixed-MoA to improve more with more samples. However, the authors do not provide this comparison. 
- The organization of the paper is a bit fragmented. Starting with the proposed method, then empirical analysis of the problem, then extensions to longer context lengths.

### Questions
Did you ever run the Figure 3 inference scaling experiments with Mixed-MoA? It seems like as only the proposals differ, the approach should still be applicable.

### Soundness
1

### Presentation
2

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
This paper introduces Self-MoA and surprisingly it found that it's better than MoA approach which combines outputs from multiple LLMs to enhance performance. 
The authors run various experiments to use various combination of proposers and aggregators and found that using only the top-performing models to generate multiple outputs and then aggregate achieve superior performance. 
Through various experiments across benchmarks, including aplacaeval 2.0, mmlu, crux and math, the authors found that focusing on quality often yields better performance than mixing diverse models, which include lower-quality outputs. 
The paper also introduce Self-MoA-Seq, a sequential variant that address the limitations of aggregating outputs when the context length is a constraint. 

The contributions are: 
- This papers introduces Self-MoA, which outperforms Mixed MoA on various benchmarks. 
- Through experiments, the authors proposed a conjecture and suggests that a core trade-off between diversity and quality can cause performance difference. 
- The authors also extends Self-MoA to Self-MoA-Seq, which mitigates the context length contraint.

### Strengths
- The paper is well written and presented. 
- Self MoA presents a practical advancement over Mixed MoA on various benchmarks.

### Weaknesses
 - The technical novelty is limited. Compared to Mixed MoA, a main difference is exploring the tradeoff between quality and diversity. Mixed MoA already uses a few sequential layers, which is somehow related to self-moa-seq.
- There is no experiment about using larger models, e.g. GPT-4o as proposer and / or aggregator. Mixed-MoA used GPT 4o as aggregator. 
- The current analysis are more of correlation analysis. Further systematic casual analysis or study on the root cause of why and when selfMoA outperforms Mixed MoA? Some studies on the aggregator's aggregation process (combining inputs from various proposers) would be helpful. e.g. attention at aggregation step. 
- typo: line 155, table 2.1 -> table 1

### Questions
- Does selfMoA only use 1 layer (if we use the notion mentioned in Mixed MoA) 
- In table 1, it seems that you use Qwen1.5-110B-Chat as the aggregator? 
- Do you have results using WizardLM-2-8x22B as aggregator, as following the findings in the selfMoA paper, would this yield better results?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper critically evaluates the importance of diversity in an ensemble of LLM responses. It chooses the general Mixture-of-Agents (MoA) method as its target of inquiry and comprehensively evaluates it against a proposed non-diverse variant called Self-MoA which achieves superior performance. They also conduct analysis on the trade-off between model diversity in an ensemble and the quality of the outputs and find that performance is most sensitive to quality. The authors also try to identify in which cases a diversity of models could be helpful. There is also an exploration of the scalability of this method of inferencing that contributes to the discussion of scaling inference compute.

### Strengths
It showcases that when you know the kind of task the model will be doing, it is better to duplicate that model rather than seek diversity, which is quite an interesting finding that might go against how some currently view LLM ensembling methods.

Their argument is sound and the structure of the paper makes sense and is quite thorough in its analysis. They use creative methods to showcase the quality-diversity trade-off and supply figures that complement their findings well. I think the paper is a good contribution.

### Weaknesses
My main issue with this paper is that it doesn't really answer the question posed in its title very thoroughly. I think a broad question like "Is mixing different LLMs beneficial?" can be broken down to answering two questions: "When does it matter?" and "When doesn't it matter?". I feel like the paper does a very good job answering the latter question with many experiments and analyses; the former, though, isn't as well covered.

Section 3.2 attempts to tackle this question by arguing that "increasing diversity can enhance MoA's performance when the quality is controlled." I feel like this claim isn't very well supported, as there is only one case that results in an increase in average performance, and it's quite minimal, as mentioned later in the section. Moreover, using the aggregate combined task here as a metric to judge whether one configuration is better than another could be misleading as it might obscure performance variations across individual tasks. This can mask specific cases where mixing models shows benefit for some tasks but not others. I don't find it to be enough to say one model is more performant than another due to it having a higher aggregate score. I think there should be some more discussion on this.

- In Table 1, what does the Individual column mean? Is it just passing the query to the model without any form of MoA? If so, what models does Mixed-MoA and 3-layer-MoA use? 
The number of forward passes of 12 doesn't seem consistent to me with the fact MoA uses 5 different models per layer (so if I'm understanding this correctly it should be 3 layers * 5 models + 3 aggregations = 18 forward passes)

- In Figure 2, I assume it's a typo and the y axis of the MATH dataset is supposed to be 1.6-2.8?

Grammar issues:

- 422-423 "we fit a linear regression to..."
- 371 "explains 70% MoA’s performance"
- 444 "WHEN MIXED-MOA OUTPERFORMS SELF-MOA?"

### Questions
- In Table 1, what does the Individual column mean? Is it just passing the query to the model without any form of MoA? If so, what models does Mixed-MoA and 3-layer-MoA use? 
The number of forward passes of 12 doesn't seem consistent to me with the fact MoA uses 5 different models per layer (so if I'm understanding this correctly it should be 3 layers * 5 models + 3 aggregations = 18 forward passes)

- In Figure 2, I assume it's a typo and the y axis of the MATH dataset is supposed to be 1.6-2.8?

Grammar issues:

- 422-423 "we fit a linear regression to..."
- 371 "explains 70% MoA’s performance"
- 444 "WHEN MIXED-MOA OUTPERFORMS SELF-MOA?"

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The work explores the effectiveness of ensembling outputs from different LLMs or the single top-peforming model. It introduces the concepts of cross-model diversity and in-model diversity, and argues that the cross-model diversity is not essentially beneficial to the model cooperation. To this end, authors presents their method named Self-MoA which aggerates the outputs from the single top-performing model rather than the diverse models. Experiments shows the superiority of Self-MoA. Further discussions are about quality-diversity trade-off, statistical  analysis, the design of Self-MoA-Seq.

### Strengths
1. An seemingly reasonable method, i.e. Self-MoA and good evaluation performance.

2. Comprehensive experiments.

### Weaknesses
1. I think the overall technical contribution of this work is limited. The idea is likely to be a combination of self-consistency and MoA. It more likes a technical report rather than a research paper.

2. It is recommended to add the introduction of Self-MoA. Readers not familiar MoA would be confused about the oveall framework.

3. In the Section 3.1, authors model the correlations between quality and diversity with linear regression. I wonder how the authors ensure the relationship should be linear, rather than polynomial or else.

### Questions
See weakness.

### Soundness
2

### Presentation
2

### Contribution
2
