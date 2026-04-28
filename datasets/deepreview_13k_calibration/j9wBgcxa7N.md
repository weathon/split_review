# MAgICoRe: Multi-Agent, Iterative, Coarse-to-Fine Refinement for Reasoning

- Decision: Reject
- Avg Score: 4.80
- Scores: 5, 6, 3, 5, 5

## Abstract
Large Language Models' (LLM) reasoning can be improved using test-time aggregation strategies, i.e., generating multiple samples for each problem and aggregating over them to find a better answer.
While these strategies improve performance, they often reach a saturation point beyond which additional samples provide no return. 
Refinement offers an alternative by using model-generated feedback to not only sample more solutions but also improve their quality. 
However, refinement introduces three key challenges:
\textbf{(1) Excessive refinement:} Uniformly refining all instances can cause over-correction and reduce overall performance.
\textbf{(2) Inability to localize and address errors:} LLMs have a limited ability to self-correct and struggle to identify and correct their own mistakes in a targeted way. 
\textbf{(3) Insufficient refinement:} Deciding how many iterations of refinement are needed is non-trivial, and stopping too soon could leave errors unaddressed. 
To tackle these issues, we propose \method{}, a framework for \acron{M}ulti \acron{Ag}ent \acron{I}teration for \acron{Co}arse-to-fine \acron{Re}finement.
\method{} aims to avoid excessive refinement by categorizing problems as easy or hard, solving easy problems with coarse-grained aggregation, and solving hard ones with fine-grained and iterative multi-agent refinement. 
To enable more granular error localization, we incorporate external step-wise reward model (RM) scores. 
Moreover, to ensure effective refinement, we employ a multi-agent loop with three agents: the \textit{Solver}, the \textit{Reviewer} (which generates targeted feedback based on step-wise RM scores) and the \textit{Refiner} (which incorporates feedback and generates new solutions).
To ensure sufficient refinement, we re-evaluate updated solutions, iteratively initiating further rounds of multi-agent refinement and making the communication between the Reviewer and Refiner agents bidirectional. 
We evaluate \method{} on Llama-3-8B and GPT-3.5 and show its effectiveness across five math reasoning datasets, with consistent gains for all datasets and models.
Across datasets, even one iteration of \method{} beats Self-Consistency by $3.4\%$ (absolute), Best-of-$k$ by $3.2\%$, and Self-Refine by $4.0\%$ while using less than $50\%$ of the samples. 
Furthermore, unlike iterative refinement with baseline methods, \method{} continues to improve with more iterations.
Finally, our ablations highlight the importance of \method{}'s use of RMs and multi-agent communication

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces MAGICORE, an inference framework for LLM reasoning that leverages a multi-agent approach with three agents: the Solver, the Reviewer, and the Refiner. The Solver generates multiple solutions, which are then scored by the Reviewer using a Process Reward Model. The Refiner subsequently refines solutions based on their quality and confidence scores. MAGICORE demonstrates superior performance over several aggregation methods.

### Strengths
1. The writing is clear and easy to follow.
2. The proposed method is efficient and straightforward, achieving better performance than self-aggregation and self-refinement methods.

### Weaknesses
1. The paper lacks a comparison with methods that also use a PRM. While baselines are based on self-aggregation and self-refinement, it remains unclear how MAGICORE would perform compared to methods like self-consistency with PRM. This omission may make the comparison in Figure 1 less conclusive.

2. The method assumes that LLMs can improve through fine-grained stepwise refinement. Adding preliminary experiments or a discussion section to validate this assumption could enhance the paper’s robustness.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
MAGICORE is a multi-agent framework designed to improve large language model (LLM) reasoning by selectively refining answers based on difficulty, leveraging external reward models (RMs) for targeted feedback and iterative refinement. This approach addresses key issues in traditional refinement methods, such as over-correction and insufficient error localization, achieving superior performance across five math reasoning datasets compared to baseline methods. Notably, MAGICORE shows continued improvement with more iterations, unlike other methods, highlighting the importance of selective and iterative refinement using RMs.

### Strengths
1. This paper proposes multi-agent framework, named MAGICORE, effectively categorizes problems into "easy" and "hard" cases, applying coarse-grained aggregation to simpler problems and fine-grained, multi-agent refinement to challenging ones. This selective refinement approach minimizes over-correction and ensures computational resources are allocated efficiently, resulting in higher performance without excessive sampling.

2. By incorporating step-wise Reward Model (RM) scores, MAGICORE significantly improves error localization, allowing for more accurate, step-by-step feedback. This targeted feedback mechanism enables the framework to address specific mistakes precisely, enhancing the overall quality of model outputs.

3. This paper conducts comprehensive experiments to verify the effectiveness of the proposed framework MAGICORE.

### Weaknesses
1.  MAGICORE relies heavily on external Reward Models to assess difficulty and provide targeted feedback, which could introduce dependency on the quality of these RMs. However, the better reward model is not easy to obtain. If the RMs are not well-tuned or suited to the specific dataset, the refinement process might misidentify errors, potentially impacting overall performance.

2. While MAGICORE shows strong results on math reasoning tasks, it is unclear how well it would perform on other types of reasoning tasks, which may have different error patterns. More evaluations should be conducted across a broader range of tasks to verify the generalizability of this framework beyond math.

3. Although MAGICORE improves with additional iterations, the optimal stopping point remains unclear, despite the authors conducting experiments with 1 to 5 iterations for validation.

### Questions
See Weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces MAGICORE, a multi-agent, iterative coarse-to-fine refinement framework designed to improve reasoning performance in LLMs. The system uses three agents—Solver, Reviewer, and Refiner—who collaborate iteratively, guided by external RMs that provide both global and step-wise feedback. The framework is evaluated on five math reasoning datasets, showing consistent gains across models and datasets, outperforming existing self-refinement and aggregation-based baselines.

### Strengths
MAGICORE combines a multi-agent system with a coarse-to-fine approach, allowing efficient resource allocation that avoids the pitfalls of excessive or insufficient refinement.

The integration of external reward models (ORM and PRM) for both global and step-wise scoring enables precise error identification and correction.

MAGICORE outperforms higher-budget baselines with fewer samples, making it a promising framework for cost-effective large-scale reasoning.

### Weaknesses
The three technical designs to address the three major challenges seem isolated and independent, making the overall framework not a “unified” solution.

Each of the three technical designs has been fully utilized by existing research works, e.g., least-to-most prompting, multi-agent discussion, and iterative refinement. This paper does not propose any fundamentally new method, limiting its technical contributions.

The selected baselines for comparison are insufficient. Several self-correction, self-refinement, tree searching, or multi-agent reasoning methods are not included.

The experiments are only conducted on math reasoning datasets, leaving several other domains unexplored, e.g., program coding, commonsense reasoning, and symbolic reasoning. These are also essential domains in LLM reasoning.

Only two LLMs are considered. Several up-to-date and more powerful models, e.g., GPT-4 and llama3 70B/405B, should also be investigated.

The paper seems too dense to read. The presentation necessitates much improvement.

### Questions
Is the MAGICORE framework suitable for other types of reasoning? What modifications would be necessary for other domains? For example, in terms of condition evaluation and the refinement process?

How does MAGICORE handle misleading questions where the Solver consistently arrives at the same incorrect answer across multiple solutions? Would MAGICORE classify such cases as 'easy,' given that only one of the ORM or PRM needs to be 'fooled' during classification?

The refinement process relies on PRM-generated step-wise scores to guide targeted feedback. How sensitive is this process to the accuracy of PRM's step-wise evaluations? If PRM incorrectly assigns high scores to flawed steps, could this lead to ineffective or even harmful refinements? How does MAGICORE mitigate such risks in error localization?

The reviewer and refiner roles are distinct, with the Reviewer generating feedback based on step-wise scores. What specific mechanisms ensure that the Reviewer’s feedback is both relevant and actionable for the Refiner? Are there cases where ambiguous or overly general feedback could hinder the refinement process?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents MAgICoRe (Multi-Agent, Iterative, Coarse-to-Fine Refinement), a framework designed to enhance the answer quality of LLMs. The framework addresses three major challenges in refining LLM outputs: avoiding excessive refinement (which can lead to over-correction), targeting error localization, and ensuring sufficient refinement. It proposes to use three agents (solver, reviewer, and refiner), and two reward models (PRM for local scores and ORM for global scores) to enhance the base model’s performance. The key idea behind the proposed framework is categorizing problems as easy or hard, solving easy problems with coarse-grained aggregation, and solving hard ones with fine-grained and iterative multi-agent refinement. The authors evaluate MAgICoRe on 5 datasets and 2 models and show that it obtains accuracy higher than weighted self-consistency.

### Strengths
The idea of incorporating RM models and selective refinement with LLMs is very interesting. 
The results are very promising, and this method seems to be better than the baselines.
The authors open source their code.

### Weaknesses
Writing
W1: The writing of Section 2 could be clearer. Some definitions of the conditions (in Appendix B) are very important to understand the method. Please move it up to the main context. This is especially true when you have a complex Figure 2. If there is no space, please move related works to the appendix.

Novelty
W2: While the reviewer appreciated the proposed framework, the classification of this method is not very clear. If we borrow the classification as used by [1], do the authors consider this work as an intrinsic or extrinsic refinement? If intrinsic, then you should not use separate RM models (instead you should finetune Llama3-8b to be your RM). If extrinsic, then this method seems less accurate than, say, RAG-assisted refinement.

W3: The framework is a combination of multi-agent and RM for selective refinement.  The novelty of the entire system may be hard to justify, as individual parts of the framework do not seem very new. For example, multi-agent is a very well-studied topic now, and in terms of selective refinement, [2] uses implicit confidence of LLM to selectively refine the response. [3] is less similar, but it also uses confidence to select which LLM to use for prediction. In the context of LLM, confidence is similar to the explicit RM (although the reviewer agrees that RM is better than confidence). However, as the authors admit in the paper, the idea of using RM is also not novel (l153).

Evaluation
W4: SVAMP is a dataset with 700 training and 300 testing samples. The paper says that the authors have evaluated the 1000 samples of SVAMP (l304), and the results (for example 78.1) do seem like that. This is problematic though. Please report the result on the test set only.

W5: Please specify the subtasks in MMLU as used. The reviewer failed to add up the numbers to 974 for the standard math-related questions (l308).

W6: Please add GPT4 for a subset of the test datasets.

W7: The cost of the proposed framework seems very high compared to decoding-only frameworks (majority voting or vanilla self-consistency). The method runs models multiple times, whereas decoding-only frameworks mainly just decode and do not run the main model. Can the authors please provide the inference delay or cost for the comparison?

### Questions
Please see the weakness above.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The authors focus on achieving reliable problem-solving with LLMs through refinement. They identify three main issues in existing refinement methods: excessive refinement, inability to localize and address errors, and insufficient refinement. To address these challenges, they propose MAGICORE, an adaptive framework designed to enhance both performance and efficiency in multi-step reasoning with LLMs by intelligently applying test-time aggregation and targeted refinement. Experimental results show that MAGICORE outperforms leading alternative approaches by a significant margin.

### Strengths
The paper is easy to follow and includes figures explaining the intuitive concept behind the proposed framework.

The authors propose a framework aiming to simultaneously address all issues in the existing refinement approaches. In particular, the authors try to design a complex process to avoid or alleviate the problems related to each issue. 

The experimental results presented in the paper demonstrate the state-of-the-art performance of the proposed framework.

### Weaknesses
1. The major issue of this paper is the lack of research focus and key insights. At first glance, the authors open a big question aiming to address all issues in the existing refinement approaches. However, this question is too big to hold for both the researcher and the reader because understanding and gaining insights into one issue to capture solid motivations may be challenging enough. For instance, in the introduction, even Figure 1 contains too much content to understand, and it is hard for me to figure out which major problem (based on your research experience) should be the most critical. Interestingly, in this submission, the authors emphasize the importance of identifying difficult problems and allocating more resources to them (i.e., 'over-correction'). However, in this paper, they present everything uniformly, making each part overly complex in both conceptual explanation and writing.

2. The consequence of presenting everything together is that, to me, the paper's main contribution to the community becomes difficult to identify. It is difficult to discern the in-depth insights the authors gained from related work that motivated their approach design. Specifically, can the authors claim that the proposed framework addresses all three issues present in existing approaches? If not, which issue does the framework address more effectively, and which one remains less resolved? If the framework can address one issue well, why and what makes this framework achieve better performance in this issue?

3. Besides, I may not fully capture the relation or connections between each module of this framework. By saying connection, I mean that why the next module is necessary after the previous one finishes. For example, after identifying hard problems based on the RM scores, why do we need to perform a complex iteration multi-agent process? Is it good enough for me to use an existing complex approach to address these hard problems? I believe this misunderstanding stems from the complexity of the framework and the authors' vague problem definition. In most moments during the paper reading, before I fully appreciate and explore a module in depth, the author has already started defining a new problem and proposing a more complex solution.

4. More importantly, with so many equally important agents involved, hallucinations could become a significant issue: if any agent produces an error, it may impact other modules. Worse, based on my experience, the issues caused by hallucinations tend to accumulate over iterations rather than being resolved. However, the authors do not discuss this obvious core drawback of LLMs. For example, some existing work suggests that their framework relies on advanced LLMs and performs poorly with weaker LLMs. The authors of this paper fail to provide such a necessary discussion.

5. Additionally, while reading the paper, I noticed that the authors provide only brief explanations without engaging in in-depth discussions before quickly moving on. As a result, I am left wondering what findings or insights, beyond these design elements, might better illuminate the corresponding issues. This is because engaging in in-depth, specific discussions rather than quickly presenting design elements should be a core focus within the community.


6. In aiming to address all three issues by incorporating these modules into the framework, the current experiments are insufficient to demonstrate its effectiveness or provide a deeper understanding. For instance, we might ask about the 'cost' of this framework. By 'cost,' I refer to the number of interactions required and the number or length of prompts needed to solve the problem. Second, a more specific ablation study may be necessary to examine the three issues in existing approaches, identifying which issue is most severe and to what extent each part of the framework addresses it. Besides, if 1-2 issues are ignored, I can remove or simplify the corresponding modules from the framework. Then, how about the performance? Third, please include more state-of-the-art approaches in the baseline, as Self-Refine may be outdated given the recent advancements in the field (refinement).


7. Last but not least, I believe this paper does not align with my preferences, as the authors seem to combine multiple novel ideas into a single framework, which can be represented as A + B + C... Due to this, in addition to lacking experience in addressing a major, well-defined problem step-by-step, I feel there are some overclaims in the paper.  --- all three issues mentioned in the paper can be addressed (again without in-depth insights).

### Questions
See weaknesses above.

### Soundness
2

### Presentation
2

### Contribution
2
