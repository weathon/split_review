# Self-Taught Evaluators

- Decision: Reject
- Avg Score: 5.40
- Scores: 5, 5, 5, 6, 6

## Abstract
Model-based evaluation is at the heart of successful model
development -- 
as a reward model for training, and as a replacement for human evaluation.
To train such evaluators, the standard approach is to collect a large amount of human preference judgments over model responses, which is costly and the data becomes stale as models improve.
In this work, we present an approach that aims to improve evaluators {\em without human annotations}, using synthetic training data only. Starting from unlabeled instructions, our iterative
self-improvement scheme generates contrasting model outputs and
trains an LLM-as-a-Judge to produce reasoning traces and final judgments, repeating this training at each new iteration using the improved predictions. Without any labeled preference data, our \ourmodel can improve 
a strong LLM (Llama3-70B-Instruct) from 75.4 to 88.3 (88.7 with majority vote) on RewardBench.
This outperforms commonly used LLM judges such as GPT-4 and matches the performance of the top-performing reward models trained with labeled examples.
\if 0
We present a recipe that enables an LLM to self-improve to become a stronger evaluator (LLM judge). Our method performs iterative reasoning preference optimization on synthetically generated preference data. Without any labelled preference data, our approach can improve a strong LLM (Llama3-70B-Instruct) from 0.754 to 0.889 on RewardBench, and TODO on MT-Bench. On RewardBench, it outperforms commonly used LLM judge such as GPT-4 and matches the performance of a top-performing reward model trained with labeled examples. 
\fi

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a novel approach to training LLMs to act as **evaluators**, or "judges," without relying on human-labeled data. The key method involves a self-supervised, iterative training process where the model generates its own **synthetic data** and **preference labels**, using these to refine its evaluative skills over multiple rounds, resulting in curriculum learning. This process allows the model to progressively improve its judgment abilities without external human supervision. In tests on benchmarks like RewardBench and MT-Bench, the self-taught evaluator achieves competitive, sometimes superior, results compared to reward models trained with human annotations.

### Strengths
- The self-taught framework presented in this paper is a quite novel. It uses an iterative self-improvement process that enables the model to independently refine its judgment skills, offering valuable insights for future research in self-supervised evaluation methods for LLMs.

- The paper is well-structured and clearly written.

- The proposed self-taught method could effectively reduces the dependency on human labeling by enabling the model to generate its own synthetic data and preference labels. It offers a scalable solution for training evaluation models for LLMs.

- The empirical results are highly promising. On competitive benchmarks like RewardBench and MT-Bench, the self-taught models match or even exceed the performance of traditional reward models that rely on human annotations, highlighting the method’s strong potential for practical applications.

### Weaknesses
 - The method has only been tested on one specific LLM variant (LLAMA3-70B-Instruct), making it unclear whether the approach generalizes well to other types of LLMs or models of different sizes and architectures.

- The process for generating contrasting synthetic preference pairs is relatively simple and lacks refinement. The prompt used to generate suboptimal responses often results in fairly static patterns, and it remains unverified whether the generated response $y^l$ is indeed worse than the original. There is limited discussion on corner cases or situations where synthetic data quality might be compromised. A more carefully crafted design for preference pairs could improve the model’s ability to distinguish subtle judgment differences.

- The paper provides limited comparison with other LLM-as-a-judge methods, relying primarily on comparisons with GPT-4-0125 while omitting other competitor models from existing literature in LLM-as-a-judge frameworks.

- The computational complexity of the iterative self-taught evaluation process is not fully discussed. Generally, this approach involves a curriculum learning process requiring multiple iterations, and further discussion on the computational demands and any associated performance gains would strengthen the analysis.

- In practice, determining the correctness of a judgment can be challenging. The proposed method relies on a fairly straightforward approach for judgment annotation, and it’s uncertain whether this consistently leads to high-quality judgments. The quality of judgments has not been independently verified.

- While the performance of the self-taught evaluator generally improves with each iteration, there are scenarios (e.g., reasoning ability for RewardBench doesn't increase as more iterations are gone through) where performance declines. More in-depth analysis and discussion on these cases would provide valuable insights, and investigating a potential upper bound for the model’s performance could also be beneficial.

- The paper lacks clarity on the amount of synthetic data needed per iteration and how performance might vary with different volumes of synthetic data. Providing guidelines on optimal data requirements for each iteration would improve the method’s practical applicability.

### Questions
-Please use \citep in place of \cite where appropriate to ensure citation consistency.

- I would consider revising the score if the paper includes a more comprehensive discussion of potential drawbacks, along with a comparison to other LLM-as-a-judge baselines.

### Soundness
3

### Presentation
2

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
This paper proposes a new way to train the evaluators for the capabilities of LLMs which relies on only synthetically generated data. The authors start with a set of user instructions which are classified and sampled to represent different categories. Then, they generate pairs of responses where one is constructed to be better than the other. First, they generate a response from the model which is going to represent a better response. Second, they prompt a LLM to modify the initial user task to be semantically similar but not identical and they generate the response for that task and this sample is going to represent a worse response in the pair. For each pair, they sample N reasoning traces and judgements with LLM-as-a-Judge and select a trace which agrees with the synthetically constructed order of the samples. This trace is then used for finetuning the model. They repeat this process iteratively by using better and better LLM-as-a-Judge models but finetuning the same original model. The experiments show that on several benchmarks their method results in a better model than the same initial model trained on human data.

### Strengths
- This paper presents an efficient method for an important problem of LLM evaluation. The method relies on synthetic data without the use of human data and thus it is easier to scale in practice.
- The presentation of the paper is very clear and it is easy to follow and find relevant information
- The proposed method is quite original, especially the component on generation of artificial pairs of responses where one element is constructed to be better than the other element.
- The experimental section contains comprehensive experiments showcasing the benefits of synthetic data over human data. The results are quite encouraging and have a potential to have an impact in the community.

### Weaknesses
 - My main concern is about using *two* language models in the experiments. While the method is presented as a "self-taught" evaluator, the actual experiments rely on the use of two models: Mistral 22Bx8 Istruct for generating the initial synthetic responses, initial judgments and categorizing the queries, and Llama3-70B-Instruct for everything else. How is the need for the second model motivated? In this case, wouldn't it be the situation of distilling the knowledge of two LLMs into one rather than being self-taught?
- Regarding the experimental section and the baselines, the authors mentioned some related work that sounds to be highly applicable in the studied setting, such as the Best-of-N method. Were there any attempts to compare against it?
- The proposed method contains many steps / components that contribute to the performance of the policy. While there are several ablations and comparisons presented in the experimental section, it would be nice to understand in which degree each component affects the solution. Specifically, the impact of the iterative training and the quality of the synthetic data needs to be better understood.
- In table 2 it seems that the performance on iteration 5 is worse than on iteration 4. Why is this the case? What is happening here?

Some minor questions and clarifications:
- When comparing against the human data, were the sizes of the datasets identical? Was the user instructions with human labels filtered in the same way (which seems to preserve more complex instructions) as the user instructions used to generate the synthetic pairs?
- In terms of formatting, I think putting brackets around citations would make it easier to read the text.
- Line 090: West->Best?
- For the understanding of the algorithm, I would like to see some examples of the "related but different" prompts and to see in what kind of answers they result. Intuitively, it is hard to make difficult comparison examples synthetically, and I would be interested to read examples from this approach
- What proportion of the traces agree with the synthetic labels over the training iterations?
- Details about the model selection (line 225-227 are not very clear)
- As far as I understand, for the final inference, there are N samples generated and the majority vote is performed for the proposed method (line 244-247). Is the same done for the baselines?
- What is the conclusion from Table 6? What combination to use, if any?

### Questions
- I would like to understand the motivation behind using two language models for different steps in the experiments. Why is it necessary? What would happen if the same model is used everywhere? How does the fact of using two models reflect on positioning the method as self-taught? How the use of an additional model should be reflected in the baselines in order to make a fair comparison?
- I would like to understand the importance of various components of the proposed method and how it compass to other existing synthetic data methods like the Best-of-N mentioned in the related work section.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a novel approach, "Self-Taught Evaluator," which enhances model-based evaluation without human annotations by using synthetic data only. The iterative self-improvement process generates contrasting outputs, curating training data from WildChat for a large language model (LLM) to improve as a judge. The authors demonstrate that this method can improve Llama-3-70B-Instruct from 75.4% to 88.3% accuracy on RewardBench, matching performance levels typically achieved with human-annotated data.

### Strengths
1. **Novel Contribution**: The paper addresses a significant challenge in model evaluation by eliminating the need for costly human annotations, which can be both expensive and quickly outdated.

2. **Technical Implementation**: The proposed solution is an end-to-end pipeline that includes data curation, iterative synthetic data generation, and model training. The training produceure is also properly outlined.  

3. **Performance**: The method shows decent performance, competing with human-annotated evaluation models and LLM judges such as GPT-4-Turbo-125.

4. **Scalability and Cost-effectiveness**: This approach offers a scalable and more affordable alternative for model evaluation, which is particularly valuable for model developers.

### Weaknesses
## Methodological Concerns

**Reliability of LLM-as-a-Judge**: The paper does not thoroughly validate the reliability of various components in the LLM-as-a-Judge system used throughout the pipeline, raising concerns about the accuracy and consistency of judgments.
   
> Line 230: To perform prompt selection, we annotate the category of each instruction with the Mixtral 22Bx8 Instruct model, using the template in Figure 7 and select 20,582 examples in the reasoning category, as we expect these to be challenging inputs.

1. *Selection and Justification of Categories*: It is unclear whether the reasoning category chosen is specific to “Knowledge and Reasoning” or includes others like "Coding" or "Social Studies." Clarifying which categories were deemed “challenging” and why, with specific examples of the types of prompts included, could strengthen the rationale behind the selection process. For instance, if the reasoning category includes coding tasks, providing examples of these specific coding prompts would be beneficial. 

2. *Assumption of Prompt Difficulty*: The choice to prioritize the “reasoning” category as the most challenging is not fully justified. Other categories like “Coding” or “Social Studies” could also be complex, and without a clear definition of what constitutes “challenging”, the selection process lacks rigor. A more detailed explanation of why reasoning prompts are inherently more difficult than other types of prompts, perhaps with a comparative analysis of different prompt types, would enhance the paper’s clarity.

3. *Lacks Validation of Categorical Classification*: The study's reliance on Mixtral 22Bx8 as a judge for classification raises concerns about potential biases and reliability. Without proper validation and ablation studies, the accuracy of the classification process and the quality of selected prompts remain questionable. Including accuracy metrics, a confusion matrix, or inter-annotator agreement scores would significantly strengthen the claims made about classification quality. Ablation on using different LLMs as judge, and comparing the resulting prompt distributions, is also desirable to ensure the robustness of the selection process.

> Line 126: We use the following prompt template which is used to generate a 'worse response' y^l. Given an instruction x and baseline response y^w generated by an instruction-following LLM as usual, this prompt is used to first generate a 'noisy' version x′ of the original instruction x, and then a best-attempt y^l at responding to x′. y^l is then treated as a poor response to x, giving a preference pair y^w_i ≻ y^l_i.

4. *Assumption of Poor Response Quality*: While the methodology treats responses from certain prompts as “worse,” the inherent biases of LLMs and potential quality variances raise questions about consistency. The paper should include a more detailed discussion on the potential for these “worse” responses to sometimes be of comparable or even superior quality, and how this variability is addressed in the training process. It is important to address how the model handles cases where the generated “worse” response is not actually worse.
5. Correct me if I am mistaken, I cannot find examples for the generation of “worse responses” anywhere in the paper, including the appendix. Examples would be helpful for further illustration. 

> Line 244: At inference time when evaluating final performance, we sample generations N times and take the final judgment to be the most common verdict.

6. *Majority Vote Methodology*: The approach of using a majority vote to finalize judgments could benefit from additional clarification, specifically on how judgments are consolidated, what impact this has on final model performance, and how the number of samples N was chosen. A discussion on the sensitivity of the final judgment to the value of N, and whether there is a diminishing return with increasing N, would be beneficial.

> Line 250: To understand the effectiveness of the proposed method, we generate synthetic judgments using the same approach but based on the following data sources.

7. *Synthetic Data Generation Steps*: The paper proceed to explain high-level steps for synthetic curation, however, lacks sufficient detail on the exact generation steps, limiting reproducibility. The paper should include a more detailed description of the prompt templates used for synthetic data generation, the specific parameters used for the LLMs, and any post-processing steps applied to the generated data.

8. *Data curation details*: It is unclear how exact the data is being curated. Starting with WildChat dataset, how many conversations were applied using the prompt selection procedure? Did the author deduplicate the dataset? Did author ran PII detection? Were multi-turn conversation being included? If multi-turn conversation are being include, how are they handled during prompt selection and judgment annotation (eg. concat all the turns)? Does the curated dataset include non-English conversation? Addressing these question and provide a detailed explanation will greatly improve reproducibility of the work. 

## Analysis Concerns

> Line 497: We further instruct Llama-3-70B-Instruct to infer the complexity (using a score of 1–5) and category of each input instruction.

9. *Validation of Complexity Inference*: Relying on Llama-3-70B-Instruct to infer prompt complexity raises questions regarding its ability to accurately gauge task difficulty. Validation experiments, such as comparing the LLM-inferred complexity scores with human annotations or other established metrics of complexity, could bolster the validity of the complexity categorization. A discussion on the potential biases of the LLM in assessing complexity would also be valuable.

10. *Presence of Simple Prompts in Curated Data*: Despite aiming to filter for challenging prompts, many simpler prompts remain, suggesting possible gaps in the selection methodology. Additional validation, such as a manual review of a subset of the curated prompts to assess their complexity, could enhance prompt filtering accuracy and provide a more robust justification for the claim that the selected prompts are indeed challenging.

### Questions
1. **Validation of Prompt Selection and Evaluation**  
   Could you provide further clarity on the categories chosen for “reasoning” and explain why they were deemed the most challenging, specifically over alternatives like “Coding” or “Social Studies”? 

2. **Judgment Selection Consistency**  
   In the data collection process, was there a standardized method to ensure that “worse responses” generated were indeed inferior? Examples of these responses, especially in the appendix, would improve understanding of this process. 

3. **Majority Vote Implementation**  
   How was the majority vote for final judgments implemented? What impact did this have on the model’s improvement scores?

4. **Synthetic Data Generation Process**  
   Could the authors provide more concrete steps for generating synthetic judgments based on additional data sources? This would aid in replicability.

5. **MT-Bench Experiment**
  Since MT-Bench is multi-turn, did the author observe any difference in the performance of the evaluator on first turn versus the second turn?

### Soundness
2

### Presentation
2

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose a new approach to training an LLM-as-a-Judge that, unlike prior work, does not need human supervision.
It can improve the judgement quality of strong instruction-tuned LLMs to be comparable to SotA judge models trained in a supervised manner.

The method utilises clever prompting to generate pairs of completions for an instruction where one is known to be preferred to the other.
Judgements with chain-of-thought reasoning are then generated from the target LLM, with correct ones being SFT trained on in an iterative procedure.

It is tested on a variety of benchmarks, along with some ablations.
The original claim is somewhat supported by the empirical evidence.

### Strengths
The problem the paper is trying to address is somewhat well motivated.

The paper is well presented, with minimal errors.

The method is reasonably well communicated, and to this reviewers knowledge, reasonably novel, extending existing work nicely.
The experimental setup is also clearly communicated, with details on hyper-parameters that would greatly aid reproducibility.

The method is tested on a variety of datasets, and using a variety of data sources.
Additionally, scores per iteration and for different subsets of the RewardBench dataset are given.
Thus, the empirical data generated to evaluate this method is extensive.

Some of the empirical evidence supports the claim that the proposed method outperforms existing SotA reward models.

The authors perform several ablations and additional analysis of their method, empirically justifying some of their design choices.

### Weaknesses
 It's not entirely clear why the method should work, especially if given many iterations.
See "Questions" section for more details.

Experimentally, it appears that the iterated training does not always help, with the score often decreasing or noisily bouncing around after the first iteration.
See Table 1 "Chat" and "Reasoning" columns, table 2, and table 5 "Chat" column for clear examples of this.
In many other columns, score does not monotonically increase with iteration.
Thus, it's not clear to what extent the iterative nature of this method provides *consistent* improvements.

From table 1, the method is beaten both overall and in the "Safety" and "Reasoning" categories by other methods.
This slightly undermines the claim that the method outperforms or matches existing top-performing reward models.

The main motivation behind training a reward model is to provide a reward signal to optimise a downstream LLM's outputs to better reflect human values.
The proposed method has not been evaluated on its ability to provide such a reward signal.
 
## Errata
* Figure 1 is not referenced in the main paper text
* Table 5 "Chat" column has the Iteration 3 element in bold, but the Iteration 1 element is highest scoring.

### questions:
 The proposed method iterates over instruction and response pairs that are generated at the start, and then fixed.
Could this not cause the model to over-fit to these specific instructions and responses, neglecting performance on others?

Since the model is being fine-tuned to re-produce its own previous outputs (with some filtering applied), how can it learn to generate better critiques?
Where is the exploration coming from, and why would it favor generating good critiques over poor ones which still agree with the ground truth?

What happens if you train an LLM to optimise the resulting reward model, especially on prompts not in the initial instruction distribution of the LLM-as-a-Judge?
Does this policy LLM then outperform LLMs fine-tuned on different sources of reward?
This seems like a very important test to run to properly verify the method.

Do you know or have any idea what happens if you include response pair construction or instruction selection as part of the iterative process?

How does the proposed method avoid model collapse, as is implied to eventually happen with these iterative recursive schemes by Shumailov et al. (2024, https://www.nature.com/articles/s41586-024-07566-y)?

Multiple seeds and computing standard error/deviation would help discern the signal from the noise in regards to whether the iterative nature of the method provides significant, consistent benefits.
The reviewer notes that this might not be possible due to computational requirements involved.

In table 2, it's not clear whether the GPT4 baseline model was using 32 sample majority vote.
Please can you clarify this, as if it is not, the results of this table seems to be misleading and making an unfair comparison.

### Questions
The proposed method iterates over instruction and response pairs that are generated at the start, and then fixed.
Could this not cause the model to over-fit to these specific instructions and responses, neglecting performance on others?

Since the model is being fine-tuned to re-produce its own previous outputs (with some filtering applied), how can it learn to generate better critiques?
Where is the exploration coming from, and why would it favor generating good critiques over poor ones which still agree with the ground truth?

What happens if you train an LLM to optimise the resulting reward model, especially on prompts not in the initial instruction distribution of the LLM-as-a-Judge?
Does this policy LLM then outperform LLMs fine-tuned on different sources of reward?
This seems like a very important test to run to properly verify the method.

Do you know or have any idea what happens if you include response pair construction or instruction selection as part of the iterative process?

How does the proposed method avoid model collapse, as is implied to eventually happen with these iterative recursive schemes by Shumailov et al. (2024, https://www.nature.com/articles/s41586-024-07566-y)?

Multiple seeds and computing standard error/deviation would help discern the signal from the noise in regards to whether the iterative nature of the method provides significant, consistent benefits.
The reviewer notes that this might not be possible due to computational requirements involved.

In table 2, it's not clear whether the GPT4 baseline model was using 32 sample majority vote.
Please can you clarify this, as if it is not, the results of this table seems to be misleading and making an unfair comparison.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces a novel approach focused on leveraging synthetic training data to enhance evaluators without the need for resource-intensive human annotations during model development. Moreover, it delves into an iterative self-training methodology and introduces an iterative self-improvement framework capable of producing contrasting outputs and training an LLM-as-a-Judge. The proposed Self-Taught Evaluator demonstrates notable performance enhancements on RewardBench.

### Strengths
(1) Writing: This paper is well-written and easy-to-understand.

(2) Method: Instead of adhering to the conventional LLM-as-a-Judge paradigm for providing judgment explanations, this paper introduces an innovative approach leveraging synthetic training data to enhance evaluators, thus avoiding the need for expensive and time-consuming human annotations during model development.

(3) Experiments: Through iterative experiments on LLama3-70B-Instruct, this paper convincingly showcases the effectiveness of the proposed Self-Taught Evaluators across RewardBench, MT-Bench, and HelpSteer2 datasets.

### Weaknesses
(1) Concerning the explanation provided in line 044 and Figure 2, could you elaborate on the methodology used to ascertain the contrastiveness of the generated synthetic preference pairs beyond the prompt instructions? Specifically, what criteria are used to ensure that the generated pairs truly represent opposing preferences, and how is this verified beyond simply relying on the model's output? It is unclear if the final verdict extraction is robust enough to guarantee contrastive pairs.

(2) The definition of "similar" in Figure 2 appears ambiguous. Specifically, while x' is deemed similar to x, the term "similar" implies a high level of relevance without strict semantic identity. The notion of similarity needs to be more precisely defined in the context of instruction modification. What specific types of modifications are allowed, and how are they controlled to ensure that the modified instruction still maintains a meaningful relationship with the original instruction while generating a contrasting preference?

(3) Several typographical errors, such as the presence of "?" in Figure 2 and line 241, have been noted.

(4) The citation format lacks consistency, as evidenced by variations between line 137 and line 139. It would be beneficial to standardize this aspect.

(5) In terms of experiments, aside from Llama, have results been obtained using different models of varying sizes? It is important to assess the generalizability of the proposed approach across different model architectures and scales.

(6) Could you provide insight into the interpretation of performance fluctuations observed in Chat and Reasoning across multiple iterations? The paper should discuss potential reasons for these fluctuations and their implications for the overall stability of the self-training process.

### Questions
Please see the weakness part.

### Soundness
3

### Presentation
2

### Contribution
3
