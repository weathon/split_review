# VideoWebArena:  Evaluating Long Context Multimodal Agents with Video Understanding Web Tasks

- Decision: Accept
- Scores: 5, 6, 8, 6, 6

## Abstract
Videos are often used to learn or extract the necessary information to complete tasks in ways different than what text and static imagery alone can provide. However, many existing agent benchmarks neglect long-context video understanding, instead focusing on text or static image inputs. 
To bridge this gap, we introduce VideoWebArena (VideoWA), a benchmark for evaluating the capabilities of long-context multimodal agents for video understanding. 
VideoWA consists of 2,021 web agent tasks based on manually crafted video tutorials, which total almost four hours of content. 
For our benchmark, we define a taxonomy of long-context video-based agent tasks with two main areas of focus: skill retention and factual retention. 
While skill retention tasks evaluate whether an agent can use a given human demonstration to complete a task efficiently,
the factual retention task evaluates whether an agent can retrieve instruction-relevant information from a video to complete a task.
We find that the best model achieves 13.3\% success on factual retention tasks and 45.8\% on factual retention QA pairs, far below human performance at 73.9\% and 79.3\%, respectively. 
On skill retention tasks, long-context models perform worse with tutorials than without, 
exhibiting a 5\% performance decrease in WebArena tasks and a 10.3\% decrease in VisualWebArena tasks. Our work highlights the need to improve the agentic abilities of long-context multimodal models and provides a testbed for future development with long-context video agents.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper introduces VideoWebArena, a benchmark designed to evaluate multimodal AI models’ abilities to process and understand long video sequences alongside text and images for completing tasks. As AI assistants increasingly need to understand video inputs to perform workflows, learn skills, and make decisions autonomously, challenges arise with maintaining temporal coherence, long-term memory, and information retrieval over extended sequences. VideoWebArena addresses a gap in existing benchmarks by focusing on these long-context multimodal capabilities, comprising 2,021 tasks with approximately 4 hours of video content. The benchmark includes 400 factual retention tasks that test information retrieval and 1,621 skill retention tasks that assess the use of in-context tutorials. Evaluations of advanced video-capable models, like GPT-4o and Gemini 1.5 Pro, show that while they exhibit basic capabilities with video content, significant gaps remain compared to human-level understanding, particularly in long-term memory and task execution. This benchmark provides a critical tool for advancing and assessing long-context video comprehension in multimodal AI.

### Strengths
It introduces VideoWebArena, a comprehensive benchmark designed specifically to evaluate the long-context understanding and multimodal reasoning of models, addressing a gap in existing evaluation tools. The benchmark includes a wide range of tasks (2,021 in total), split between factual retention and skill retention tasks, which test both memory retrieval and the application of learned information.

The study provides valuable insights by evaluating prominent video-capable LLMs like GPT-4o and Gemini 1.5 Pro, showcasing their current performance levels and identifying specific challenges they face. It effectively points out the significant gap between human capabilities and the current state-of-the-art in long-context video understanding, thus paving the way for targeted improvements in AI development.

### Weaknesses
The paper’s focus on evaluating models using video records, rather than interactive environments, introduces several limitations. This approach confines the assessment to passive information retrieval and task completion without testing an agent’s adaptive capabilities in real-time. Consequently, it fails to simulate dynamic, interactive challenges where agents need to respond to changing conditions and feedback, limiting the benchmark’s applicability for real-world scenarios. Additionally, video records do not fully capture the complexity of decision-making in live environments where agents must process incomplete or misleading information. 

The paper does not specifically address potential biases related to the content of the videos used in the VideoWebArena benchmark, which raises concerns about the inclusivity and fairness of the evaluation. If the content records primarily reflect cultural, linguistic, or social contexts from a limited demographic, this could introduce biases that affect the model’s performance and generalization capabilities. Such biases may skew the results, favoring models trained on similar datasets while disadvantaging those that have been exposed to more diverse inputs. Additionally, there is the risk that the benchmark may not adequately represent ethnic and cultural variations in how information is presented or interpreted, limiting its applicability for global use cases. Addressing potential ethnic or cultural content biases is crucial for ensuring that the models evaluated can fairly and effectively serve users from diverse backgrounds.

### Questions
refer to above concerns

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents VideoWebArena, a novel, open-sourced video-based benchmark, designed to evaluate the capabilities of long-context multimodal agents in video understanding tasks. The dataset consists of 2,021 tasks based on four hours of video tutorials across six domains. Moreover, the paper conducts experiments to validate that the current intelligent agents do not perform well on most the task, and is important to the relevant research field.

### Strengths
1.	This paper provides a novel video benchmark that is very welcome to the research community.
2.	The benchmark offers a well-defined taxonomy that focuses on two main areas: factual retention and skill retention, which test different facets of a model's abilities to retrieve information from videos and efficiently apply learned skills.
3.	The paper conducts experiments to validate that the current intelligent agents do not perform well on most the task, leading to future improvement.

### Weaknesses
1.	The used LLMs are all closed-source, thus may cause obstacles to reproduction. Experiments on open-sourced intelligent agents may be included.
2.	This paper does not provide a comparison or discussing over itself and other similar video benchmarks, like MVBench[1], with respect to some tasks like temporal reasoning, etc.

[1] Li, K., Wang, Y., He, Y., Li, Y., Wang, Y., Liu, Y., ... & Qiao, Y. (2024). Mvbench: A comprehensive multi-modal video understanding benchmark. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 22195-22206).

### Questions
1.	Can new tasks or new domain be easily added into the benchmark?
2.	Through analysis, what is the possible aspects that the existing agent can be improved?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper present VideoWebArena (benchmark) to evaluate a model's ability to process long video sequences alongside text and images to complete tasks that require memory retention, information retrieval, multimodal reasoning, and skill retention. Moreover, this papaer show that these models are still a far reach from human levels of performance, highlighting a wide gap in the information retrieval and agentic abilities of current state-of-the-art long-context models.

Strengths:
+ This paper construct a benchmark called VideoWebArena.
+ The idea of this paper is novel and interesting.
+ This paper test many retention tasks, I think it is a hard task and the author complete this task.
 
Weakness:
+ Can author release the source code for this paper, I would like to try this agent.

### Strengths
See Summary

### Weaknesses
See Summary

### Questions
See Summary

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents the VideoWebArena benchmark to evaluate the capabilities of long context multimodal agents. The tasks are divided into factual retention and skill retention. The authors evaluate GPT-4o and Gemini-1.5-pro on their benchmarks and provide an in-depth analysis.

### Strengths
+ The proposed benchmark is valuable to the community.
+ The task designs make sense to me (divide into skill retention and factual retention), which challenge current modes’ capabilities to extract information from a demonstration video to complete tasks.
+ The experimental findings are insightful, especially Table 7, which suggests that current models struggle with “learning” from tutorial videos, in contrast to humans.

### Weaknesses
+ The introduction lacks references.

+ While the related works section reviews a few agent benchmarks and long-context benchmarks, it is suggested to include a dataset comparison table of VideoWA with existing benchmarks. This would clarify VideoWA’s distinctiveness, highlighting differences in task diversity, domain, video length, etc., against existing ones. 

+ To improve clarity, it would be helpful for the authors to explicitly discuss how VideoWebArena differs from VisualWebArena and WebArena in terms of environment and task design. Are there methodological innovations in this paper beyond extending these benchmarks to long videos?

+ Could the authors further clarify the difference among video agent, frames agent and summary agent in terms of their input? Does the difference lie in audio input (gemini directly takes audio while gpt-4o takes audio transcriptions)? What about the summary agent?

+ In Table 4, the example provided for temporal reasoning appears more like a counting task; substituting it with a clearer example focused on temporal reasoning might improve clarity.

+ The benchmark only evaluates Gemini and GPT-4o. I wonder why the authors do not include open-source VLMs such as LongVILA, and LLAVANextVideo (as mentioned in the intro).

### Questions
Overall, this paper offers a useful benchmark with valuable insights for the community.  However, the current presentation is not clear and many clarifications are needed. Please refer to weaknesses for my questions.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors present VideoWA, a benchmark designed to assess the capabilities of long-context multimodal agents, particularly their ability to understand and utilize video information to accomplish tasks on web-based platforms. The paper emphasizes the gap in existing benchmarks, which predominantly focus on static image or text inputs, and seeks to bridge this with comprehensive video-based task evaluation.

### Strengths
1. The paper is clearly written, with well-structured sections that guide the reader through the motivation, methodology, and results.
2. The experimental setup and evaluation in the paper are robust, employing a range of state-of-the-art models such as GPT-4o and Gemini 1.5 Pro. The results are well-documented and provide clear evidence of the limitations of current models in handling long-context multimodal inputs. 
3. The significance of this work lies in its potential to drive advancements in the development of long-context multimodal models. Although some tasks may not fully justify the necessity of video tutorials, identifying more suitable tasks that would effectively leverage the richness of video input remains a challenge. Nevertheless, the benchmark's foundation provides a valuable starting point for refining task design and exploring the benefits of video-based learning in AI agents.

### Weaknesses
Major problems I have found are as follows:
1. One significant concern is that the contributions of VideoWA appear to be relatively incremental compared to prior work such as WebArena and VisualWebArena. While the inclusion of video content does enhance task complexity and data richness, the paper does not convincingly demonstrate how these video tutorials meaningfully improve agent learning or task performance. Specifically, some tasks, like “buying the cheapest item” as presented in Table 4, do not seem to justify the necessity of video input. Agents could reasonably complete these tasks with textual intent or static images. This raises doubts about whether the chosen tasks fully exploit the potential advantages of video tutorials or merely add unnecessary complexity.
2. Another perplexing issue is the low success rate of human performance on seemingly straightforward tasks. The authors report that these metrics were gathered using the authors themselves, who should be well-acquainted with both the data and the tasks. The review questions how the human success rate could be so limited (e.g., 73.9% on factual retention), suggesting a potential shortcoming in task design or evaluation methodology. If even familiar humans struggle, it may reflect an underlying flaw in the task construction or evaluation criteria, which could compromise the benchmark's real-world applicability and reliability.
3. The paper presents an unexpected and concerning trend where multimodal models, even when provided with video tutorials, perform worse than models without them. This result contradicts the assumption that video tutorials should aid skill retention, as evidenced by the drop in performance on WebArena and VisualWebArena tasks (5% and 10.3% decreases, respectively). The authors should address whether the noise introduced by video information or ineffective agentic reasoning mechanisms is the primary cause of these shortcomings. Without further investigation or hypothesis testing, the paper leaves this critical aspect unresolved.

### Questions
Please refer to the weakness 1-3.

### Soundness
3

### Presentation
3

### Contribution
2
