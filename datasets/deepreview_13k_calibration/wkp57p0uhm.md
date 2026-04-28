# WebCanvas: Benchmarking Web Agents in Online Environments

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 6, 5, 5

## Abstract
For web agents to be practically useful, they must adapt to the continuously evolving web environment characterized by frequent updates to user interfaces and content.
However, most existing benchmarks only capture the \textit{static} aspects of the web. 
To bridge this gap, we introduce \webcanvas, an innovative online evaluation framework for web agents that effectively addresses the dynamic nature of web interactions. 
\webcanvas contains three main components to facilitate realistic assessments:
(1) A novel evaluation metric which reliably capture critical intermediate actions or states necessary for task completions while disregarding noise caused by insignificant events or changed web-elements.
(2) A benchmark dataset called Mind2Web-Live, a refined version of original Mind2Web static dataset containing 542 tasks with 2439 intermediate evaluation states;
(3) Lightweight and generalizable annotation tools and testing pipelines that enables the community to collect and maintain the high-quality, up-to-date dataset.
Building on \webcanvas, we open-source an agent framework with extensible modules for reasoning, providing a foundation for the community to conduct online inference and evaluations. Our best-performing agent achieves a task success rate of 23.1\% and a task completion rate of 48.8\% on the Mind2Web-Live test set. 
Additionally, we analyze the performance discrepancies across various websites, domains, and experimental environments. We encourage the community to contribute further insights on online agent evaluation, thereby advancing this field of research.\footnote{Our platform, tool and dataset are publically available at \url{https://www.imean.ai/web-canvas} and \url{https://huggingface.co/datasets/iMeanAI/Mind2Web-Live}}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper is devoted to the development of new benchmark for web agents, which should demonstrate flexibility and tolerance to (1) alternative (non-canonical) trajectories of task completion and (2) dynamic nature of the web, where sites and their features constantly evolve.
 
The key idea of the paper is to introduce “key nodes” in the task completion process, which designate the inevitable intermediate states of requests and URLs.

### Strengths
The motivation and the problem are very relevant

### Weaknesses
The technical quality of the work is under concerns. The work relates to evaluation methodology, and the main contribution is the proposed benchmark based on key nodes. I expect an analysis of how the proposed metric for web agents correlates with the goal metrics such as success rate based on outcomes. We can annotate, for a number of agents, outcome results for a representative number of tasks, and compare the correlation between “key nodes-based success rate” and outcome-based success rate against the same correlation for “step-based success rate” proposed in Deng et al., 2024.

This is a common requirement for new metrics in methodology papers: to look at the directionality, see e.g. “Using the Delay in a Treatment Effect to Improve Sensitivity and Preserve Directionality of Engagement Metrics in A/B Experiments” by Drutsa et al.

Table 3: the result itself is expectable, because mindAct is based on direct finetuning to ground-truth actions, which are then used for evaluation of success rate in the offline setting. Such approach makes MindAct less generalizable to flexible metric and dynamic environment, unlike GPT-3,5/4, which are used with in-context learning, without finetuning.

### Questions
Why GPT-3,5/4 perform better in the more challenging online setting as compared to offline setting (Table 3)? It is not clear what was the protocol for online setting in this table. Authors only said that “evaluation metrics … differ” and, in online setting, “we evaluate the intermediate state, not the referenced action”. Is this metric exactly “Task Success Rate” described in Section 3.2?

### Soundness
2

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
This paper proposes Webcanvas ,a benchmarking framework for evaluating web agents in dynamic online environments. In this framework, a new metric is proposed based on 'key nodes'. Then authors construct a online and dynamic dataset called Mind2Web-Live, which builds upon the existing Mind2set dataset. Mind2Web-Live includes extensive annotation data collected through human labor and will be regularly updated and maintained by authors. Finally, various models are evaluated on Mind2Web-Live, providing some insights according to the results.

### Strengths
- Introduces a innovative evaluation framework WebCanvas for web agent. By focusing on “key nodes”, this framework provides a more reliable and accurate assessment compared to traditional methods that only consider the final task success rate.
- Constructs a online and dynamic benchmark Mind2Web-Live that is an enhanced version of the original Mind2Web static dataset. 
- The authors have developed a community-driven platform where users can report issues with the dataset, and regular updates are performed.

### Weaknesses
 - When the data size was reduced from Mind2Web's original 2000+ tasks to 500 +, the authors did not analyze how many different domains the Mind2Web-Live can cover and whether there are enough tasks for each domain. Specifically, the paper lacks a detailed breakdown of the number of tasks per domain and subdomain, making it difficult to assess the benchmark's representativeness and diversity. This is crucial for evaluating the generalization capabilities of web agents across different types of websites and tasks.
- There is a problem of scalability in this dataset because updating data requires people to maintain it. When the scale of dataset increases, maintenance costs will increase. The reliance on manual annotation for key nodes and task validation introduces a bottleneck that could limit the dataset's growth and long-term viability. The paper does not provide a clear strategy for how the maintenance process will scale with an increasing number of tasks and websites, or how the annotation effort will be managed to ensure consistency and quality.

### Questions
1. Can you provide more details about the data distribution in the benchmark. Such as how many domains this benchmark can cover?  and how many task in each domain?
2. Whether the agent running in the real word environment will have a negative impact on related websites?

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
3

### Summary
This paper presents a novel benchmark for web-based tasks designed for agent evaluation. The proposed benchmark introduces step-wise assessment, live sample testing, and a user-friendly community platform, facilitating the online evaluation of agents. The authors conduct experiments using several large language models (LLMs) on the proposed platform.

### Strengths
1. The paper contributes a significant new benchmark for web mining, which is expected to provide substantial value to the research community.
    
2. The benchmark incorporates several valuable features, including intermediate state evaluations, a user-friendly interface with plugin support, and access to live datasets.
    
3. The writing is clear and well-structured, with numerous case studies that aid in understanding the framework and its applications.

### Weaknesses
1. The experimental evaluation is limited to a comparison with Mind2Web. It would be beneficial to include comparisons with additional benchmarks, evaluating a wider range of models to yield deeper insights.
    
2. The paper lacks a detailed breakdown of the sample categories. Providing statistical information on the task categories would help demonstrate the scope and coverage of the benchmark.
    
3. The benchmark currently offers a relatively small set of tasks. Expanding the sample size in future iterations would improve the benchmark's applicability. Compared to benchmarks like Mind2Web and WEBLINX, the proposed benchmark’s dataset remains limited.
    
4. Although the authors highlight their community-driven platform and a cost-effective bi-monthly data maintenance schedule, the benchmark project appears less active. Notably, the last update was two months ago, and several long-standing issues remain unresolved.

### Questions
1. Will the heatmap for evaluation function accuracy across annotation steps be generated automatically upon completion of the evaluation? This could provide users with useful insights into model performance. Additionally, could some textual analysis be offered through LLM integration?
    
2. Are all key nodes weighted equally in the evaluation process?
    
3. Could you clarify why there are no cases labeled as "value include" in Figure 5?
    
4. A minor note: The planning prompt specifies a requirement for "JSON blob format," which seems somewhat contradictory, as JSON is typically string-based, while a blob refers to a binary object. Could you clarify this distinction?

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
3

### Summary
This paper introduces a novel framework for assessing web agents in dynamic online environments. In contrast to conventional benchmarks that focus on static web conditions, WebCanvas proposes a novel key-node-based evaluation metric, an enhanced dataset named Mind2Web-Live, and efficient annotation tools. Additionally, the authors demonstrate their best-performing agent in the Mind2Web-Live dataset and provide the analysis of the performance discrepancies.

### Strengths
+ This paper is mostly well-written and easy to follow.
+ The paper is technically sound with most claims supported sufficiently by experimental results.
+ The proposed evaluation metrics and datasets seem novel.

### Weaknesses
 - The problem formulation is incomplete in Section 2. The authors should bring some contents in Section E.1 back to the main paper. Additionally, the final objective function is missing in Section 2 as well.
- It is a bit odd that “include match” and “semantic match” share the same evaluation targets for step score. Not sure if it is better to introduce additional aspects to distinguish them.  
- Some parts of the presentation could be improved, e.g., in Line 136, the notation of action history a_{1}^{t-1} is not clear. It is better to use a_{1:t-1} to represent history following POMDP literature.

### Questions
- The problem formulation is incomplete in Section 2. 
- The authors might consider bringing some contents in Section E.1 back to the main paper. 
- The final objective function seems to be missing in Section 2.
- “include match” and “semantic match” share the same evaluation targets for step score. Consider introducing additional aspects to distinguish them.  
- Some parts of the presentation could be improved, e.g., in Line 136, the notation of action history a_{1}^{t-1} is not clear. 
- It is better to use a_{1:t-1} to represent history following POMDP literature.

### Soundness
2

### Presentation
3

### Contribution
2
