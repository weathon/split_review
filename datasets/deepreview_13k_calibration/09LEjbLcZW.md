# AutoKaggle: A Multi-Agent Framework for Autonomous Data Science Competitions

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
Data science tasks involving tabular data present complex challenges that require sophisticated problem-solving approaches. 
We propose AutoKaggle, a powerful and user-centric framework that assists data scientists in completing daily data pipelines through a collaborative multi-agent system. 
AutoKaggle implements an iterative development process that combines code execution, debugging, and comprehensive unit testing to ensure code correctness and logic consistency. 
The framework offers highly customizable workflows, allowing users to intervene at each phase, thus integrating automated intelligence with human expertise.
Our universal data science toolkit, comprising validated functions for data cleaning, feature engineering, and modeling, forms the foundation of this solution, enhancing productivity by streamlining common tasks. 
We selected 8 Kaggle competitions to simulate data processing workflows in real-world application scenarios. 
Evaluation results demonstrate that AutoKaggle achieves a validation submission rate of 0.85 and a comprehensive score of 0.82 in typical data science pipelines, fully proving its effectiveness and practicality in handling complex data science tasks.ai/AutoKaggle.io/}}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces AutoKaggle, a pipeline to automatically solve Kaggle Competitions. The authors use 5 subparts in a row: a reader, a planner, a developer, a reviewer, and a summarizer. They use LLMs with RAG to develop code-based solutions, with code running, units tests. They evaluate their method on 5 Kaggle competition benchmarks.

### Strengths
**Interesting problem.** With the LLMs (+RAG) becoming mature, the open source study of their integration into broader tools that can directly be applied to data science tasks, is the natural next step.

**Overall good presentation.** Even if some details are lacking to grasp the authors' exact contribution (notably in the figures), the overall presentation clearly demonstrates the problem and the approach set up to tackle it. 

**Interesting metrics and ablation studies.**

### Weaknesses
 **Lacking evaluation.** The evaluation is lacking comparison to existing AutoML baselines (*e.g. [1]) or explanations on why the authors are not comparing their method to any existing solution. If running such comparison is not possible at all, then the authors should provide explanations on why this is not feasible. 
While detailed reports are provided on their methods and the different components, as this works apply existing techniques, its evaluation is its core contribution. 
The authors should report (at least) the standard deviation, but e.g. violin plots to compare AutoKaggle's results of other kaggle competitors could help clearly situate where this automatic pipeline stands.

**Evaluation on a (previously) unknown dataset.** It seems that AutoKaggle has been designed to solve these datasets, so one cannot evaluate how much this method would transfer to another, previously unknown dataset.
It would be nice to provide the reader with how much out of the box your method is, maybe with a user study. It seems like its your core contribution, so having independent people trying AutoKaggle and commenting on how easy the setup and interaction is on a left out dataset would help people looking for such solutions.

**Figure 2 could be improved.** The figure could be split to separate the overall pipeline from details on some of its components. Most importantly, what part is using an LLM, what part is using a human expert ? This figure represents 70% of what the reader is looking for, it should provide first the overall intuition, and then enough details on specific core components that you want to highlight.

**You related work section is actually a background section.**
Your current related work covers some domains that are integrated within AutoKaggle. It thus feels more like a related work of your background section (what AutoKaggle builds upon). Is there any *e.g.* AutoML method that you can compare to ? Any method that addresses the same issue ?

### Questions
* Did you do any finetuning over the used models, notably LLMs or are you using frozen models ?
* Why cannot you compare to any existing baselines ?
* Have you optimized the creation of your pipeline using these 5 kaggle competitions, or have you left out some of them, to evaluate on competitions you did not know at design time ?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents AutoKaggle, a multi-agent framework specifically designed to handle the complexities of Kaggle data science competitions.  The framework organizes the competition workflow into six distinct phases—background understanding, exploratory data analysis, data cleaning, in-depth exploratory analysis, feature engineering, and model development and validation—allowing agents to work systematically through each stage. Key agents, including Reader, Planner, Developer, Reviewer, and Summarizer, collaborate within this structure, with iterative debugging and unit testing to ensure robustness and accuracy in code generation. AutoKaggle integrates a machine learning tools library to streamline tasks, enhance code reliability, and provide users with educational insights through comprehensive reports at each phase. Evaluated across multiple Kaggle competitions, the framework achieved an average completion rate of 83.8% and ranked in the top 42.8% in Kaggle.

### Strengths
- AutoKaggle introduces a tailored phase-based workflow with multi-agent collaboration specifically designed for data science competitions. The system’s demonstrated high average completion rate and competitive ranking in Kaggle highlight its effectiveness, particularly in tabular classification and regression tasks, showing its strength in handling structured data challenges.

- AutoKaggle empowers the Developer agent to perform iterative debugging and unit testing, bolstering the robustness of code generation. Additionally, the integration of a comprehensive machine learning tools library improves the system's efficiency and accuracy, making it better suited for tackling complex Kaggle competitions

### Weaknesses
 - Limited novelty.  While the paper addresses data science problem-solving using LLM-based agents, it lacks a clear description of the specific challenges it intends to solve that existing methods have struggled with. Extending from a single-agent to a multi-agent system is insufficiently justified in this field, as the necessity and performance gains of such an approach are not clearly demonstrated. Existing works, as mentioned in the introduction, have also tackled similar problems with LLM-based agents, questioning the incremental contribution of AutoKaggle.

- Multi-agent system design. The multi-agent system, including agents like Reader, Planner, Developer, Reviewer, and Summarizer, is insufficiently explained in terms of its collaborative structure. It is unclear whether these agents operate in an assembly-line fashion or if they engage collectively in each phase under the "Cooperative Engagement" label in Figure 1. Further clarification on their integration and interdependence within each workflow phase is needed.

- Role clarity of Planner and Summarizer. Given AutoKaggle’s sequential, phase-based workflow, the necessity of a Planner agent is ambiguous. Can you quantify the contribution (such as on completion rates or error reduction) of this Planner agent in your system? Similarly, the Summarizer’s role in contributing to critical performance metrics such as completion rate or Best Normalized Performance Score, is not explicitly justified, leaving its impact on performance uncertain.

- Unit Test and Debugging. Dose the Developer agent generate dataset-specific unit tests that align with each unique code snippet or not? How the Developer agent adjusts unit tests based on code variations to ensure logical consistency and accuracy across different tasks? 

- Lines 275-276 mention the importance of detecting logical errors in code, yet the method for achieving this is underexplored. Can you explain more details about detecting the logical error? More detail is needed on how logical errors are detected and avoided, as conducting exploratory data analysis or statistical checks after data cleaning or feature engineering alone may be insufficient. 

- Table 2 illustrates the system's performance across different debugging attempts (DT), showing how increased debugging impacts metrics like Completion Rate (CR) and Comprehensive Score (CS). The data indicate that both CR and CS improve as DT rises, reflecting enhanced task completion and accuracy with more debugging opportunities. What the 'performance plateaus' mean  in line 524-525?

- The paper does not provide information on the cost of running AutoKaggle, which is essential for evaluating its performance and practical applicability. It's benifit to provide cost and total runtime to understand the performance. 

- The chosen baselines are not entirely convincing. Recent similar works, AIDE[1] and MLE-Agent[2] have shown remarkable capability in Kaggle competition settings. A comparative analysis with these recent works, particularly focusing on AutoKaggle’s unique advantages in effectiveness, efficiency, or other performance metrics, would highlight its distinct contributions to the field.

- A broader evaluation across various task types such as time series prediction, image classification, and text classification, are necessary, as these are critical and challenging categories in Kaggle competitions. The current experiments focus primarily on tabular datasets, leaving it unclear whether AutoKaggle is capable of handling more complex, domain-specific tasks. Can AutoKaggle complete such tasks? 

- What is the requirement of the LLM? Can AutoKaggle works well with gpt-3.5 or other open-sourced models?

### Questions
Please refer to the questions in Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a scaffolding framework which uses LLMs to create a multi-agent system, used to attempt Kaggle problems. They use a "phase-based" multi-agent approach, together with a library of hand-crafted ML tools, and extensive hand-crafted unit-tests tailored to the Kaggle problems.

Applying this framework to 8 Kaggle problems (4 pre-GPT-4 training cut-off, 4 afterwards), they achieve a significant solve rate, and an average of 42% on the Kaggle leaderboard.

The paper also explores ablation of various modules (various tools, and the unit-testing module).

### Strengths
A system which can score 43% on Kaggle leaderboards is a significant milestone on the path to automated coding and datascience. Additionally, since many challenges which such a system would face would also arise in more general task-completion (e.g. long-term planning, establishing coherency, managing context, preventing execution from looping) and so would transfer to improve AI agents in general.

Great collection of Classic and Recent challenges, and baselines seem reasonable (though see my Q about the Strong Baseline).

It's helpful to have this variety of scores (though see my Q about CS).

Architecture is clearly laid out, and the paper is overall very easy to read.

Clear exploration and explanation of the underlyring readon why the feature-engineering tools reduce the framework's score (many features, leading to more complexity than the agents can handle).

### Weaknesses
Whenever CoT is used as an interpretability tool, I think it's always wise to mention unfaithfulness e.g. https://arxiv.org/abs/2305.04388

There are two places where a long list is hard to read:
#1 ~L78: AutoKaggle integrates a comprehensive machine learning tools library, covering three core toolsets: data cleaning, feature engineering, and model building, validation, and prediction.

#2 ~L186: The data science process is divided into six key stages: understanding the
background, preliminary exploratory data analysis, data cleaning, in-depth exploratory data anal-
ysis, feature engineering, and model building, validation, and prediction

Perhaps "model-building, -validation, and -prediction" would be easier to read.

~L146: I'm surprised not to see mentioned what seems to me to be the main thing underlying the motivation of multi-agent systems: finite context length, requiring summarisation and specialisation.

It's not clear how much of the headline 43% on the leaderboard is down to the skill of the human-in-the-loop, which severely undermines the claim. Without a comparison to how well the human takes unassisted (in terms of success rate or time taken), or to how well AutoKaggle performs without HITL, it's impossible to reliably state how effective the framework is.

Unspecified HITL also undermines the various claims of a "fully automated framework" (e.g. L175)

Not much detail on these unit tests. Who writes them? What's the coverage like? Are there any guarantees? If (as I suspect) the "meticulously designed" unit tests are written by humans, then we have a similar situation as with the unspecified human-in-the-loop: the framework is not "fully automated", and it's impossible to rigorously determine how much effect the human hand-holding has on the framework's suggess. This should, at minimum, be clearly, explicitly and boldly acknowledged.

Additionally, it is unclear to me how much of the ML-tools library was developed alongside particular Kaggle Competition attempts. If the tools were developed on a case-by-case basis, to address hurdles found in the challenge, then there is significant data leakage from the evaluation dataset to the framework, leading to overfitting to the competitions chosen during development, and much of the headline 43% comes from tools handcrafted by human developers on a case-by-case basis. For a fair validation of how well this framework performs in "fully automated" mode, the library would need to be "frozen" while the framework was tested on a held-out set of Kaggle Competitions.

Very minor point: ~L350, I agree that there is a risk of data leakage for competitions from before Oct '23, however to say that GPT-4o's training data includes Classic Kaggle is an assumption: better to say simply that there is a risk of data leakage.

If you're considering data leakage, it would be worth flagging that the 42% includes Classic problems: using only the newer problems, performance is slightly below human average.

### Questions
~L140, you say that CoT improves reasoning at the expense of introducing hallucinations. Is there any evidence that CoT makes models any more or less likely to hallucinate?

~L141, you say that the ReAct paradigm addresses hallucinations - that's not my understanding of what ReAct does or how it works, my understanding is that it combines thoughts and actions, yes, but that this has nothing to do with hallucinations or refining outputs.

~L360: What is the difference between "Success - Non-compliant" and "Success - Compliant"?

~L403: What's the justification / motivation for the complex / compound "Comprehensive Score"? How does it compare to other measures, what specifically does it achieve or avoid?

~L431: could you say more about this "strong baseline" - I don't understand its construction.

If adding FE tools drops performance because FE adds too much complexity, then why does "All tools" (which presumably includes FE tools) recover this performance?

### Soundness
2

### Presentation
3

### Contribution
3
