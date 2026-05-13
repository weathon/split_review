# Beyond In-Context Learning: Enhancing Long-form Generation of Large Language Models via Task-Inherent Attribute Guidelines

- Decision: Reject
- Scores: 6, 5, 6, 6, 6

## Abstract
In-context learning (ICL) is an important yet not fully understood ability of pre-trained large language models (LLMs). It can greatly enhance task performance using a few examples, termed demonstrations, without fine-tuning. Although effective in question answering, ICL often underperforms in long-form generation tasks such as summarization. Under appropriately realistic assumptions, we empirically and theoretically show that ICL demonstrations alone are insufficient to teach LLMs the task’s language and format distributions for generation.
We argue for explicit exposure to the task distributions and hypothesize that defining them by prompting enhances model performance. To this end, we present LongGuide, which efficiently generates two parallel streams of guidelines capturing task language and format properties: (i) Metric Guidelines (MGs) that instruct models to optimize self-evaluated metrics; and (ii) Output Constraint Guidelines (OCGs) that constrain generation at both token and sentence levels. LongGuide automatically selects the best combination of guidelines, improving both strong open- and closed-source LLMs by over 5% in both zero- and few-shot settings. We show that LongGuide is generalizable, learnable by weak models to enhance strong ones, and integrates synergistically with automatic prompt optimizers.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
ICL usually use demonstration examples to improve the LLM's performance.  In this paper, the authors propose LongGuide (§3), a guideline- learning algorithm that efficiently1 generates two types of guidelines concurrently from limited task training data as supplementary instructions to enhance LLMs: metrics guidelines and output constraint guidelines.

### Strengths
- the paper demonstrate the complementary values of guidelines; and propose two kinds of guidelines: metrics guidelines and output constraint guidelines.
- the paper proposed a full algorithm to learn guidelines from task training dataset. and show improved performance on multiple datasets of different tasks
- The paper did a through ablation study and investigation/evaluations to study the impact of guidelines.

### Weaknesses
 - There exist many advanced automatic prompt optimization algorithm based on a training dataset, the authors only include APO, and I think they should include some more recent methods as baselines. So that we can have a better understanding the usefulness of this method.
- the automatic metrics are out-of-dated e.g. using Rouge scores for summarization. The authors can use LLM as judges to show the improvement.
- human evaluate datasets in Figure 5 is small where only 50 examples.

### Questions
- Please add some more recent algorithms in automatic prompt improvement as baselines.
- Please include some LLM-based evaluation method to compare the long-form generation instead of rouge and bleu scores.

### Soundness
3

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
4

### Summary
In-context learning for generation tasks requires the model to capture some attributes of the desired output texts. The paper introduces a method, LongGuide, to more effectively use in-context examples for generation tasks by first using a small set of examples to develop guidelines about the desired output format, then providing these guidelines (generally in addition to the ICL examples) during inference. The guidelines are divided into two sets: metric-based guidelines, developed by using ChatGPT evaluation along axes of generation quality and selecting axes that human answers perform highly along; and statistics-based guidelines, generated from properties of the human answers (e.g. average length). LongGuide provides additional gains on top of ICL and prompt optimization.

### Strengths
S1. The idea of providing explicit task guidelines is well-motivated and clearly effective; I like the breakdown into metric-oriented and output-text-statistics oriented guidelines, which to the best of my knowledge is novel. 

S2. The method is more effective on stronger models (likely because these models are better at instruction following). Surprisingly, it's also somewhat effective on weaker, non-instruction-tuned models (line 1036).

S3. The authors are thorough in their analysis, specification of hyperparameters, and description of the setting. I also appreciate the specification of annotator wages.

### Weaknesses
W1. I feel that the formalization in Section 2 is not rigorous and frankly distracting from the goals of the paper. While I can see some benefit to stating Remark 2.1 given that some of the literature makes different assumptions, I feel the assumptions provided to start the proof are not well-formed and the property as a whole does not feel terribly useful. Remark 2.2 seems wholly unnecessary, as it seems to essentially claim that you will consider your method better than the baseline if it outperforms the baseline on the metrics. This does not require a proof.

W2. While the attributes are computed using up to 50 train set examples, the model is not evaluated on using 50-shot ICL, which feels like a natural baseline to consider. Recent works on long-context ICL have demonstrated improved performance with many demonstrations.

W3. The use of ROUGE and BLEU as the final downstream metrics seems ill-advised. These are both very simple ngram metrics, without the expressiveness of other metrics; the fact that they show near-identical trends (line 368) is unsurprising because they measure very similar things.

### Questions
Q1: Can you elaborate on the aims of the formalization / theoretical claims in section 2? I am not clear on the reasoning for this section.

Q2: The point about the guidelines not being useful for tasks the models are trained on is an interesting claim (line 556 onwards). Could you verify this with a model with open training data?

Q3: In regards to the title: are these texts really "long-form"? Certainly they are generation rather than classification, but the outputs for most of these tasks are quite short. 

Q4. The evaluation in 4.1 establishes the goal as minimal Jensen-Shannon divergence between the score distributions of gold summaries and model answers. Is this a good goal? Is it possible that the model answers are better on some axes than human answers, and this fails to account for this setting?

Minor presentation notes:
* the jump to notation in lines 36-45 was abrupt and it's not clear at this point in the paper why establishing this notation is useful; it might be better to introduce this in section 2.
* the use of "metrics" in line 101 reads a bit strange; I would refer to these as properties, which you evaluate using ChatGPT.
* showing the % gain is not super helpful in table 2, and it clutters the table.
* lines 478-485 about the ablations performed would have been useful to know earlier, since earlier tables reference these settings. 
* formatting typo in the citation of Krippendorff's alpha (line 431)
* unclear what "the mode of 17 response tokens" means in line 123
* typo in line 1015: "second not the sam"
* in Figure 17, skipping step 2 seems to improve the performance, not worsen it?
* the formatting of links to appendix figures is a bit non-standard

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores the ICL capabilities of LLMs, pointing out that relying solely on ICL is insufficient for effectively completing long-form generation tasks, and provides experimental validation and theoretical analysis to support this claim. Based on these findings, the authors propose a hypothesis: optimizing multiple text property tasks can approximate the overall goal of optimizing long text generation tasks. To this end, the authors design the LongGuide to generate two types of guidelines to enhance the performance of LLMs, and validate its effectiveness through a large amount of experiments.

### Strengths
1. The proposed method is grounded in a well-established conclusion supported by both experimental and theoretical evidence, providing a solid basis for its formulation.
2. The effectiveness of LongGuide has been confirmed through a number of experiments, demonstrating its significant performance improvement in multiple long-text generation tasks.
3. The article provides a solid theoretical analysis explaining why LongGuide can better achieve task objectives.

### Weaknesses
1. The LLM's selection of metrics is based on the distribution of its pre-training data, which may lead it to favor common or general metrics. Introducing human verification on top of this could be more effective.
2. I believe the novelty of this method is limited, as there are already some automated prompt designs for long-form generation [https://arxiv.org/html/2406.14449v1, https://arxiv.org/abs/2211.01910]. In certain cases, the LongGuide method can only choose not to use any guidelines in the final step.

### Questions
1. When calculating the JS.Avg metric, the authors used ChatGPT to score two responses, but the paper does not provide a specific display of the prompt used.
2.  In the final step of the method, there are only four choices—use MG, use OCG, use both, or use neither. Can a more sophisticated strategy be designed to leverage the advantages of both? For example, considering the requirements of MG and OCG in different stages rather than simultaneously.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces LongGuide, to efficiently generate two parallel streams of guidelines capturing task language and format properties. All the experiments are conducted on finetuned LLMs (Mistral/ ChatGPT), which is a major concern without isolating ICL capacity from Instruction following capacities. I don't get the point of mentioning In-Context Learning in the name. 

I like the theoretical derivations given in Section 2.1. But it is not solid. I don't buy in that 4.1 is a strong proof of Hypothesis 2.1. 

Specifically, the discussion on the weights of different objectives are pretty weak. Manual preference on different aspects of generated long-context are actually always highly unbalanced based on queries and contents. The theory basically ignores the unbalanced and dynamic weights on different objectives and simply treats them the same. 

The metrics and datsets used for evaluating LongGuide are pretty weak.  

Additionally, the work is pretty much only a prompt work with little solid science contribution. The prompt workflow itself is also only based on weak hypothesis and cannot intuitionally matches the manual work pattern. For manual workflow, I refer to human writer's working pattern. Human writer doesn't write based on a given metrics collection and keeps reviewing it. Intuitionally it is not solid for me. Take novel writing as an example, as a reader, sometimes I pay more attention to whether the writing is good, sometimes I pay more attention to storyline. I don't always assign 0.9 weight to storyline and 0.1 weight to writing.

### Strengths
1. Good writing.
2. Motivation is clear.
3. Their ablation studies on each elements of their method in the appendix are detailed and clear.

### Weaknesses
 The paper introduces LongGuide, to efficiently generate two parallel streams of guidelines capturing task language and format properties. All the experiments are conducted on finetuned LLMs (Mistral/ ChatGPT), which is a major concern without isolating ICL capacity from Instruction following capacities. I don't get the point of mentioning In-Context Learning in the name.

I like the theoretical derivations given in Section 2.1. But it is not solid. I don't buy in that 4.1 is a strong proof of Hypothesis 2.1.

Specifically, the discussion on the weights of different objectives are pretty weak. Manual preference on different aspects of generated long-context are actually always highly unbalanced based on queries and contents. The theory basically ignores the unbalanced and dynamic weights on different objectives and simply treats them the same.

The metrics and datsets used for evaluating LongGuide are pretty weak.

Additionally, the work is pretty much only a prompt work with little solid science contribution. The prompt workflow itself is also only based on weak hypothesis and cannot intuitionally matches the manual work pattern. For manual workflow, I refer to human writer's working pattern. Human writer doesn't write based on a given metrics collection and keeps reviewing it. Intuitionally it is not solid for me. Take novel writing as an example, as a reader, sometimes I pay more attention to whether the writing is good, sometimes I pay more attention to storyline. I don't always assign 0.9 weight to storyline and 0.1 weight to writing.

### soundness:
 2

### presentation:
 3

### contribution:
 2

### strengths:
 1. Good writing.
2. Motivation is clear.
3. Their ablation studies on each elements of their method in the appendix are detailed and clear.

### weaknesses:
 1. For the proof in Section 2.1, it is well-written but only a descriptive math. Remark 2.1 and Definition 2.1 only have weak relationship with hypothesis 2.1. And Hypothesis 2.1 only claims a simple thing: Task T can be optimized by optimizing several understandable aspects of the task, e.g. fluency, factuality, and etc. Noted that each aspect is with a fixed L in their setting. They don't give a solid proof for that. Intuitionally it is not solid for me. Take novel writing as an example, as a reader, sometimes I pay more attention to whether the writing is good, sometimes I pay more attention to storyline. I don't always assign 0.9 weight to storyline and 0.1 weight to writing.

2. The metrics reported in Section 4.1 is pretty weak, with only BLEU-1/ ROUGE-L given and without more clear and specific evaluation aspects related to human, like fluency, factuality, and etc. If human evaluation is not accessible, at least LLM-based evaluation should be given. Although they provide BERTScore, but it is actually similar to BLEU-1/ ROUGE-L on the evaluation aspects. It is mainly based on similarity. They should move more detailed analysis or some estimations of the manual evaluation in the appendix to the main context.

3. There is little direct takeaway from the paper. By direct takeaway, I mean that engineers and researchers can directly adopt the hyper-parameters and models given from a paper to their academic and industrial pipeline. The experiments conducted in the paper only cover SAMSum/ CNN/ SWiPE in the main text, which are not comprehensive and challenging at least for nowadays research.

### questions:
 I don't get the point of mentioning ICL in the paper's name. Because they only adapt instruction tuned LLMs in their research. And a lot of existing research points that there is a trade-off between the instruction following capacity and ICL. Maybe more experiments on base models are needed.

### flag_for_ethics_review:
 ['No ethics review needed.']

### rating:
 6

### confidence:
 3

### code_of_conduct:
 Yes

### role:
 Review

### Questions
I don't get the point of mentioning ICL in the paper's name. Because they only adapt instruction tuned LLMs in their research. And a lot of existing research points that there is a trade-off between the instruction following capacity and ICL. Maybe more experiments on base models are needed.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a study on LLMs' generation quality using in-context learning showing its ineffectiveness on long-context tasks, and proposed a new technique, LongGuide, to alleviate the problem.
LongGuide is an algorithm to generate customized guidelines for the LLM to optimize a set of imposed self-evaluated metrics. Overall, LongGuide collects a set of task-independent metrics, obtains the verbal descriptions of metric values via LLM self-evaluation and combines them with constraint-based guidelines which instruct the model on the numerical properties such as token/sentence count.

The technique is evaluated on a set of long-form generation tasks (summarization, text simplification, machine translation, generation) against SoTA prompt optimization algorithms such as APO and adv-ICL.
The experiments show that LongGuide improves LLMs' performance across the board, working both for medium-sized models (Mistral-7B-it) and large ones (ChatGPT 3.5 Turbo) - as shown via automatic metrics (BLEU, ROUGE-L) and human evaluation.

### Strengths
* a new method for automatically finding a set of LLM guidelines that improve longform generation is proposed
* it outperforms prompt optimization SoTA algorithms on a series of benchmarks, both for medium-sized and large models
* in addition to introducing the algorithm, the authors conduct an extensive study on how in-context learning is ineffective for longform generation

### Weaknesses
 * metrics used as the core set of LongGuide are described insufficiently - the main thing explained about them is that they do not include LLM-based ones which sounds worrying since those are proved to have correlation with human judgements, at least for summarization tasks they're superior to the numeric ones like ROUGE-L
* with a combination of metric guidelines and output constraint guidelines evaluated at the last step of LongGuide, there arises the question on performance/cost aspects of LongGuide and how it compares to prompt optimization SoTA - I couldn't find it in the main paper content
* l. 208: "...and propose 12more metrics for a broader evaluation coverage" - where are they described?

### Questions
l. 208: "...and propose 12more metrics for a broader evaluation coverage" - where are they described?

### Soundness
4

### Presentation
4

### Contribution
3
