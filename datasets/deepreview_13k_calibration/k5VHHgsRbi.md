# MME-RealWorld: Could Your Multimodal LLM Challenge High-Resolution Real-World Scenarios that are Difficult for Humans?

- Decision: Accept
- Avg Score: 6.80
- Scores: 8, 6, 8, 6, 6

## Abstract
Comprehensive evaluation of Multimodal Large Language Models (MLLMs) has recently garnered widespread attention in the research community. However, we observe that existing benchmarks present several common barriers that make it difficult to measure the significant challenges that models face in the real world, including: 1) small data scale leads to a large performance variance; 2) reliance on model-based annotations results in restricted data quality; 3) insufficient task difficulty, especially caused by the limited image resolution. To tackle these issues, we introduce \abbr. Specifically, we collect more than $300$ K images from public datasets and the Internet, filtering $13,366$ high-quality images for annotation. This involves the efforts of professional $25$ annotators and $7$ experts in MLLMs, contributing to $29,429$ question-answer pairs that cover $43$ subtasks across $5$ real-world scenarios, extremely challenging even for humans. As far as we know, \textbf{\abbr is the largest manually annotated benchmark to date, featuring the highest resolution and a targeted focus on real-world applications}. We further conduct a thorough evaluation involving $29$ prominent MLLMs, such as GPT-4o, Gemini 1.5 Pro, and Claude 3.5 Sonnet. Our results show that even the most advanced models struggle with our benchmarks, where none of them reach 60\% accuracy. The challenges of perceiving high-resolution images and understanding complex real-world scenarios remain urgent issues to be addressed. The data and evaluation code are released in our Project Page.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces MME-RealWorld, a large-scale, fully manually annotated benchmark for multimodal large language models across diverse real-world tasks. The MME-RealWorld has 13366 images with 29429 question-answer pairs annotated by humans. It covers 43 subtasks across 5 real-world scenarios. MME-RealWorld is the largest manually annotated benchmark to date, featuring the highest resolution and a targeted focus on real-world applications. It reports comprehensive results with various leading LVLMs.

### Strengths
1. MME-RealWorld is the largest manually annotated benchmark for LVLMs across 43 subtasks across 5 real-world scenarios.

2. MME-RealWorld has the highest resolution among manually annotated benchmarks. 

3. It reveals several insights for current LVLMs. For example, existing models still lack abilities for image detail perception and dynamic information understanding.

### Weaknesses
Overall, the proposed MME-RealWorld is a solid paper. There are some additional comments:
1. The holistic MME-RealWorld is too large for developing LVLMs. The author should formulate a mini set of MME-RealWorld for community convenience. I suggest maintaining a balance of task types and difficulty levels while reducing the overall size
2. There exists a clear preference for preparatory APIs for selecting E or refusing to answer the question. Does this mean the preparatory APIs are better aligned with human values and have better AI security? The author may discuss if it is possible to compare preparatory APIs with open-sourced models in a better way. Moreover, I suggest that the authors conduct a detailed analysis of when and why models choose option E or refuse to answer.
3. MME-RealWorld has a large scale of images and question-answer pairs. The author should discuss if MME-RealWorld is sufficiently diverse or just collecting several similar images and QAs. More comparisons on the distribution of image types, question types, and answer types between MME-RealWorld and other benchmarks are welcomed. 
4. It is better to have a discussion of knowledge leakage LVLMs on MME-RealWorld benchmark, as in [1].

### Questions
Overall, the proposed MME-RealWorld is a solid paper. There are some additional comments in Weakness section.

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
4

### Summary
This paper analyzes the limitations of existing MLLM benchmarks and observes three significant challenges (i.e., small data scale, restricted data quality of model-based annotations, and insufficient task difficulty especially caused by the limited image resolution). To address these issues, this paper constructs a new benchmark named MME-RealWorld that is the largest manually annotated benchmark to date and features the highest resolution and a targeted focus on real-world applications. The authors benchmark 29 advanced MLLMs on the introduced MME-RealWorld, revealing the limitations of existing MLLMs (none of them reach 60% accuracy).

### Strengths
+ The overall paper is well organized and easy to follow. The motivation of constructing the dataset is clear.
+ This paper contributes a large-scale, large-resolution and manually annotated VQA dataset, which contains 13,366 high-quality images and 29,429 question-answer pairs covering 43 subtasks across 5 real-world scenarios.
+ Large number of MLLMs are benchmarked on the introduced benchmark, i.e., 4 close-source and 25 open-source MLLMs in total.

### Weaknesses
 - Although the dataset contribution is great, it is hard to find some insightful analysis from this paper. The authors only summarize the benchmark results. It would be better to provide more in-depth analysis and highlight the future direction.
- In Lines 479-480, the authors claim that ‘This indicates that most models’ visual perception modules fail to identify the objects in the images corresponding to our questions.’ This is not clear and convincing. I am wondering how do the authors attribute the higher frequency of ‘E’ outputs to the limited image detail perception of MLLMs? 
- In Lines 481-485, the authors analyze the ‘limitations of MLLMs in understanding dynamic information’ without providing any qualitative or quantitative result. It would be more convincing to provide some evidences to support such statement. 
- Figure 2a shows the different domains and tasks. It would be nice to add a figure to show the distributions of different domains and tasks for better readability.
- In Lines 93- 94, the authors claim ‘we collect a total of 13, 366 high-resolution images from more than 300K public and internet sources.’ I have doubts about the number of the data sources. 300K is a huge number, and how long does it take to collect the images?
- For better readability, it would be better to add a paragraph title for the last paragraph in Section 3.3.

### Questions
Please refer the Weaknesses.

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
This paper presents a new evaluation benchmark for Multimodal Large Language Models (MLLMs), dubbed MME-RealWorld, which focuses on challenges that models face in the real world. Specifically, MME-RealWorld covers 29,429 question-answer pairs across 5 real-world scenarios. Experimental results on MME-RealWorld show that even the most advanced models still struggled in real-life scenarios. Besides, the authors have also conducted detailed analyses to explain the unsatisfying performance of MLLMs.

### Strengths
- The perspective of evaluating MLLMs in real-life scenarios, such as OCR in the Wild, Video Monitoring and Autonomous Driving is new and of significant value for practical deployment of MLLMs.
- The authors have conducted detailed comparisons with existing benchmark in Tab.2, which helps better capture the unique characteristics of MME-RealWorld.
- The authors have evaluated 24 open-sourced MLLMs and 4 closed-sourced MLLMs, which provide a comprehensive evaluation of current MLLMs.

### Weaknesses
 - The evaluation on MME-RealWorld seems to require lots of computation resources, which may limit the accessibility for researchers with fewer resources.

### Questions
Do the authors have plans to expand or adapt MME-RealWorld to include new tasks or modalities as MLLMs capabilities evolve?

### Soundness
3

### Presentation
4

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
In this paper, the authors present the MME-RealWorld dataset which stands out for a few key reasons. First, it’s the largest human-annotated benchmark for real-world scenarios with nearly 30,000 QA pairs created by 32 volunteers. The data is high quality, featuring high-resolution images that capture important details and every annotation was double-checked by a professional team. The tasks in this dataset are challenging, reflecting real-world needs that even top models struggle to handle accurately. The authors also include a Chinese section in their dataset with 5,917 QA pairs to avoid translation and cultural issues.

In addition, the authors evaluate a total of 24 open-source MLLMs (some of which are public APIs) on QA pairs that emphasize perception capabilities, reasoning, and a focus on Chinese. They share insights into the strengths and limitations of current models, showing that even the most advanced ones struggle with these benchmarks, with the top ones achieving high 50s%.

### Strengths
The dataset is a comprehensive and high-quality collection of realworld QA pairs manually annotated to capture complex details and ensure accuracy. It features high resolution images essential for interpreting information in certain domains like MO, with annotations rigorously cross-checked by small group of professionals. The dataset includes particularly challenging, real-world tasks, where top models struggle to handle, with performance generally falling below 60% accuracy. Additionally, a dedicated Chinese section addresses translation and cultural gaps often seen in other datasets. Finally, an evaluation of numerous open-source models highlights current limitations in handling such complex, real-world scenarios.

### Weaknesses
The dataset is certainly valuable and a step forward compared to existing QA-focused benchmarks. However, the contribution may be somewhat limited for publication in this conference due to a few areas. For instance, the diversity of data sources appears limited, with an overemphasis on specific tasks like autonomous driving (If the goal is to capture embodied understanding, related areas in robotics could also be included to broaden the dataset’s scope) Similarly, the monitoring section could benefit from a more varied range of examples and so on. There is not a discussion on why these areas are chosen over others. While tackling everything can be challenging, my worry is that this dataset will introduce bias toward certain domains while trying to address limitations of other benchmarks. 

The use of multiple-choice challenges, while popular, remains a somewhat limited way to assess model capabilities. A more open-ended evaluation method would provide a richer assessment of model understanding, especially on this complex benchmark. The addition of a fifth option in multiple-choice questions is a positive step, but more could be done to move beyond predefined answers.

Additionally, the reliance on full human annotation restricts scalability. It would be beneficial if the authors leveraged this benchmark as a foundation to extend to larger datasets and broader domains. 

Finally, while English and Chinese are the primary languages in current benchmarks, including more languages would strengthen the dataset’s multilingual utility.

### Questions
Do authors have plans or see it feasible to increase diversity of data sources and tasks? Is the pipeline on data collection, labeling and evaluation scalable? can you easily extend to other languages and data sources? from the current version it looks very manual and not scalable. It would be good to share more insight as extending the dataset to more image sources and languages, even in future, would be great. (please refer to my comments in the previous section)

Can we add more open ended evaluation methods? Moving beyond fixed options, or providing more open-ended tasks without predefined answers, would allow for a deeper evaluation of model understanding.

### Soundness
3

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
This paper introduces a new benchmark dataset, MME-RealWorld, designed to evaluate the capabilities of Multimodal Large Language Models (MLLMs) in handling high-resolution, real-world scenarios. The dataset addresses limitations in existing benchmarks, such as small data scale, reliance on model-based annotations, and insufficient task difficulty. MME-RealWorld contains over 13,000 high-quality, high-resolution images annotated with 29,429 question-answer pairs across 43 subtasks and 5 real-world scenarios, making it the largest manually annotated benchmark to date. The paper reports the performance of 29 prominent MLLMs on this benchmark, revealing that even the most advanced models struggle to achieve 60% accuracy, indicating significant challenges in perceiving high-resolution images and understanding complex real-world scenarios.

### Strengths
- 1) The MME RealWorld proposed in this paper has significant advantages in terms of data scale, annotation quality, visual content resolution, language types, task types, and task domain diversity, filling the gaps in existing work. It emphasizes the relevance of benchmarks and the real world, providing a strong and persuasive benchmark for evaluating the visual-language abilities of multimodal agents in real-world application-related scenarios.

- 2) The experimental section of this paper is solid. The authors present rich test results and analysis, providing various statistical indicators to reveal the limitations of existing VLMs in fine-grained image perception and dynamic information understanding, as well as biases of models from different sources in visual-language tasks. This offers valuable insights for improving the performance of VLMs in various application scenarios.

### Weaknesses
 - 1) The main challenges of MME RealWorld stem from high-resolution images and complex content. However, the corresponding questions are only focused on image content recognition and simple single-step reasoning, showing limitations in task difficulty and the requirement for understanding capabilities of large models.

- 2) Some methods displayed on the leaderboard are restricted by fixed input resolutions. In high-resolution scenarios, directly resizing input images may result in the loss of information needed to answer questions. Therefore, is the model's error due to the inability to find the correct information from complex image content or because the necessary information was not provided at the input stage? Supplementing such discussions can further enhance the persuasiveness of the paper.

### Questions
- 1) In line 315, the paper says "InternVL-2 demonstrates the strongest perception abilities, outperforming other closed-source models.", but Tab.3 shows that Qwen2-VL is the best performing model. So is there a typo here? Please point out if I've misunderstood.

- 2) It is recommended to add the max resolution supported by the baseline model to the table to enhance readability.

### Soundness
3

### Presentation
3

### Contribution
3
