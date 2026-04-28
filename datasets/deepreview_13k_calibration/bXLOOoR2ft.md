# DoraemonGPT: Toward Solving Real-world Tasks with Large Language Models

- Decision: Reject
- Avg Score: 6.75
- Scores: 8, 8, 5, 6

## Abstract
The field of developing AI agents is advancing at an unprecedented rate due to the powerful capabilities of large language models (LLMs). However, current LLM-driven agents mainly focus on solving tasks for the image modality, which limits their ability to understand the dynamic nature of the real world, making it still far from real-life applications, e.g., guiding students through multi-step laboratory experiments and identifying their mistakes. Considering the video modality better reflects the ever-changing and perceptually intensive nature of real-world scenarios, we devise DoraemonGPT, a comprehensive and conceptually elegant system driven by LLMs to handle dynamic video tasks. Given a video with a question/task, DoraemonGPT begins by converting the input video with massive content into a symbolic memory that stores task-related attributes. This structured representation allows for spatial-temporal querying and reasoning by sub-task tools, resulting in concise and relevant intermediate results. Recognizing that LLMs have limited internal knowledge when it comes to specialized domains (e.g., analyzing the scientific principles underlying experiments), we incorporate plug-and-play tools to assess external knowledge and address tasks across different domains. Moreover, we introduce a novel LLM-driven planner based on Monte Carlo Tree Search to efficiently explore the large planning space for scheduling various tools. The planner iteratively finds feasible solutions by backpropagating the result’s reward, and multiple solutions can be summarized into an improved final answer. We extensively evaluate DoraemonGPT’s effectiveness and reasoning capabilities in real-world dynamic scenarios and provide in-the-wild showcases demonstrating its ability to handle more complex questions than previous studies.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work introduces a system called DoraemonGPT, which is an LLM-driven agent handling video-driven tasks. It first decomposed the video based on spatio-temporal relations and questions. Furthermore, it plans an action sequence based on a Monte Carlo tree search.  Just like humans use external knowledge to plan better, DoraemonGPT can access external sources like search engines, textbooks, databases, etc. When deconstructing tasks into spatial and temporal dominant memories, it will only store them related to the task. These memories are stored in a table, and LLM can query it using symbolic language. A series of sub-task tools are designed to simplify memory information querying. Each tool focuses on different kinds of spatial-temporal reasoning by using individual LLM-driven sub-agents with task-specific prompts and examples. In order to effectively navigate the large planning domain, DoraemonGPT uses MCTS. By choosing a highly expandable node to extend a new solution and backpropagating the answer's reward, the planner iteratively discovers viable answers.

### Strengths
* It is very novel to combine a symbolic memory database with an MCTS planner using LLMs to solve video-based tasks.
* provides detailed information about prompts, experiments conducted, and analysis results. These are useful in assessing the DoraeGPT's potential.

### Weaknesses
 * Considering many models like BLIP, YOLOv8, PaddleOCR, and other models for extracting the information for video. It is not clear how shortcoming these models affects DoraemonGPT. 
* Works like Yu et al. achieved better performance on NEXT-QA (zero-shot) than DoraemonGPT.

### Questions
* Can't model like BLIP and along with a model which takes a query and features of the frames from BLIP figure which frames are relevant to the query? Why TSM is required?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Paper introduces a novel approach for video understanding and spatial-temporal reasoning. From the high level, it first builds a symbolic, spatial-temporal knowledge base given a video using several off-the-shelf tools. Next, this approach utilizes a pre-trained LLM as a planner to interactively invoke tools including canonical SQL query, search, etc for retrieval-augmented generations, and novel sub-task tools that break down the original query into sub-questions like "what", "how", etc. Results on the challenging NExT-QA dataset demonstrate the clear advantages of the proposed method against both end-to-end baseline and counterpart LLM-assisted approaches.

### Strengths
+The topic studied here is important. Augmenting the powerful LLMs with better tools and smarter planning skills is crucial to unleash their full potential and also open up new applications in, for example, multimodal domains. I believe this paper could drive interest to a broad range of audiences from canonical multimodal learning and LLM communities.

+The method is technically sound. Building a symbolic knowledge base first, and then invoking an LLM-based system to query it make sense especially when it comes to complicated multimodal data like videos. Decomposing the original query into sub-questions also looks like a promising approach upon to canonical LLM tool-use, where the tools are limited to search, SQL query, etc.

+The results on the challenging NExT-QA data are impressive.

### Weaknesses
Having said those above, I have the following major concerns and I hope the authors could provide some clarifications:

-It seems that all baselines in table 2 are "straight-through" compared to the proposed approach, that is, they are either end-to-end, or simply produce several sub-queries, and invoke the corresponding tool directly, while none of them have a separate stage of building the spatial temporal symbolic database. Therefore, I do think a more fair comparison should also take the time cost of building such a database into consideration. At least, some additional details should be outlined, ex. how long does it take to build a symbolic database in average? How does this compare to the overall inference time of the baselines? These are the questions that will help with a better understanding on the proposed method.

As a side note, can the proposed method still work without a pre-built database? I think some of the queries can be done directly by invoking the right tool, ex. VideoQA, no?

-The authors have claimed that their approach is "an intuitive yet versatile system driven by LLMs that is compatible with various foundation models and real-world video applications.". However, it was only evaluated on one dataset and it might raise concern on the generality of the proposed approach. I have to admit that I am not an expert in video understanding but maybe the following datasets should be considered for additional evaluations: [1-2].

-Some references in LLM + planning (and tool use, memory) are missing [3-5]

### Questions
See "weaknesses"

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents DoraemonGPT, an LLM-based system to handle dynamic video tasks. Given a video with a question/task, DoraemonGPT first converts the input video into a symbolic memory for spatial-temporal reasoning by sub-task tools. The authors then incorporate plug-and-play tools to assess external knowledge and address tasks across different domains. Finally, an LLM-driven planner based on MCTS is used to explore the large planning space for scheduling various tools. DoraemonGPT’s effectiveness and reasoning capabilities is demonstrated in one dataset, i.e., NExT-QA.

---
The authors' feedback addresses most of my concerns, I increased my score (also considering other reviewers' comments).

### Strengths
1. Clear presentation. The reviewer can easily follow most of the paper, especially the methods and experiments.  

2. Novel idea that MCTS is used to explore the large planning space for scheduling various tools.  

3. Good performance on the evaluated benchmarks with strong baselines.

### Weaknesses
1. Overclaim. With a performance of about 50% acc on only one test dataset, the authors claim "toward Solving Real-world Tasks", which is a n good example of overclaim in the reviewer's opinion.  In fact, real-world has many types of tasks, even solving all dynamic video tasks, it is not equal to " Solving Real-world Tasks".  The current performance on NExT-QA, while promising, is far from demonstrating a general solution to real-world tasks. The claim should be more carefully contextualized to reflect the actual scope of the work, which is primarily focused on a specific type of video understanding task.

2. No sufficient related works and the motivation is not clear. The authors say that "current LLM-driven agents mainly focus on solving tasks for the image modality", so they study dynamic video tasks. It can been seen that the authors totally ignore the large number of other LLM-driven agents that are not related with image/video at all, e.g., [1,2,3,4]. The motivation for focusing solely on dynamic video tasks is not well justified, especially considering the broader landscape of LLM agents that tackle diverse problems outside of visual modalities. The paper should provide a more comprehensive overview of related LLM-based agents, including those that do not focus on vision, to better position the contribution of this work.

3. The evaluation can be more convincing if more datasets are used. The current evaluation relies on a single dataset, NExT-QA, which limits the generalizability of the findings. While the performance on this dataset is a good starting point, it is not sufficient to demonstrate the robustness and versatility of the proposed approach. The lack of evaluation on other video understanding datasets makes it difficult to assess the true capabilities of DoraemonGPT across different task types and video content.

### Questions
The are many overclaims and no sufficient related works and the motivation is not clear. It is clearly below the bar of ICLR. The reviewer encourage the authors reformulate their paper writting (Authough I like the concrete ideas proposed in this paper).

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces "DoraemonGPT", an LLM-based system tailored for video question-answering. DoraemonGPT utilizes different pretrained expert models to extract various video information and convert it into texts that can be understood by LLM. DoraemonGPT saves this information into an external symbolic memory module with a space-dominant (SDM) component and a time-dominant (TDM) component. 
In addition, DoraemonGPT relies on LLM to decompose a task into subtasks. It defines a set of subtask tools to solve subtasks. 
The research further explores the role of the MCTS planner in searching for the best subtask decomposition.
Experimental results show that DoraemonGPT can outperform other LLM-based systems like ViperGPT and VideoChat on the video QA dataset NExT QA.

### Strengths
- The proposed symbolic memory system and the MCTS planner on video tasks are new.
- The paper is easy to understand.
- Experiments show that it can outperform other LLM-based systems like ViperGPT.

### Weaknesses
 - The evaluation set is small. The paper only conducted experiments on a subset of the original NExT QA dataset. In addition, for the ablation study, the system was evaluated on 3 question types, each with 10 questions only. 
- The authors mentioned that the small size of the evaluation is caused by the budget limit. This might suggest that the method is expensive. I think the paper should include a discussion about how many tokens the system consumes, and how much this system costs to answer a question on average.

### Questions
- How long does the inference take to answer a question on average? Given the complexity of the methodology, this information is important for users.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
