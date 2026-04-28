# TestAgent: An Adaptive and Intelligent Expert for Human Assessment

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 5, 6

## Abstract
Accurately assessing internal human states is critical for understanding their preferences, providing personalized services, and identifying challenges in various real-world applications. Originating from psychology, adaptive testing has become the mainstream method for human measurement. It customizes assessments by selecting the fewest necessary test questions (e.g., math problems) based on the examinee's performance (e.g., answer correctness), ensuring precise evaluation. However, current adaptive testing methods still face several challenges. The mechanized nature of most adaptive algorithms often leads to guessing behavior and difficulties in addressing open-ended questions. Additionally, subjective assessments suffer from noisy response data and coarse-grained test outputs, further limiting their effectiveness.
To move closer to an ideal adaptive testing process, we propose TestAgent, a large language model (LLM)-empowered adaptive testing agent designed to enhance adaptive testing through interactive engagement. This marks the first application of LLMs in adaptive testing. To ensure effective assessments, TestAgent supports personalized question selection, captures examinees' response behavior and anomalies, and provides precise testing outcomes through dynamic, conversational interactions.
Extensive experiments on psychological, educational, and lifestyle assessments demonstrates that our approach achieves more accurate human assessments with approximately 20\% fewer test questions compared to state-of-the-art baselines. In actual tests, it received testers' favor in terms of speed, smoothness, and other two dimensions.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper describes an LLM based agent system designed to perform human assessments in an optimal manner. Optimal meaning as few questions as necessary to achieve an accurate assessment. The assessment is applied using chat interaction with the user. The system dynamically selects questions, represents the users performance (cog. diagnosis), and attempts to identify and correct for various anomalous answers via open ended elaboration. Report generation is also covered.

### Strengths
The idea here is good and the solution is comprehensive. At a high level the authors are proposing to use LLMs to perform human assessment vs. using existing rigid approaches. This intuitively makes sense, but of course is not straight forward due to the inclusion of a potentially unreliable model. 

Representing the users performance based on previous answers, and using this representation to implement anomaly detection is an interesting concept. In general the anomaly detection component is compelling.

The focus on various types of evaluation is helpful, particularly the identification of error modes.

### Weaknesses
The Universal Data Infrastructure is not well defined, I came away not really understanding this component. Please revise the description with a focus on clarity. Specifically cognitive diagnosis training. The description lacks detail on how the domain is determined, how it is represented, and how it is used. Furthermore, the process of simulating students using GPT is unclear. What do the prompts look like? How much data is generated? Concrete examples are needed. Finally, the origin of the a, b, and c variables in the cognitive diagnosis model is not explained.

The major weakness here is that using an LLM introduces a new problem, namely LLM hallucinations leading to misrepresentation of results.  The authors bring up this up in section 3.8. It would be worthwhile for the authors to discuss the trade off between the introduction of hallucinations and the issues of traditional testing that originally spurred the work.

The multidimensional evaluation omits many details necessary to determine it validity i.e. how is accuracy determined? Controls for ordering and bias? Significance tests.

### Questions
What kind of model is the cognitive diagnosis component? What data is it trained on and how is it applied? getting very concrete here will help.

How was accuracy determined in the multidimensional evaluation?

### Soundness
3

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
This work introduces TestAgent, an LLM-based adaptive testing agent. TestAgent has dynamic question selection capabilities, an autonomous feedback mechanism and anomaly management module, and the ability to generate detailed diagnosis reports. The authors use student data from MATH education, personality tests, and mental health testing. As part of the results, the authors present simulation-based evaluation results, a case study with Test Agent, and a human study with volunteers to interact with TestAgent.

### Strengths
- The work attempts to tackle an important problem of human measurement. It seems like a good idea to leverage LLM-based agents for this purpose. 
- The work tries to study their proposed systems through a series of simulated and real-world experiments.

### Weaknesses
 - Overall, the writing and organization of the paper are hard to follow and thus make it hard to provide a nuanced assessment of the submission. There are also many typos throughout the work—please proofread carefully. The remaining comments will talk more about suggestions for improving the presentation of methodology as well as recommendations for evaluation clarity.
- What exactly is being measured through human assessments is unclear throughout Section 2, i.e. what is exactly captured by $\theta$ and what are concrete examples as defined by the datasets considered in the experimental section? Specifically, it is unclear how the abstract concept of 'ability' is operationalized in each of the different datasets (MATH, MBTI, and mental health). For example, in the MATH dataset, is $\theta$ a single scalar representing overall math proficiency, or a vector capturing different sub-skills? Similarly, for the MBTI and mental health datasets, what specific traits or constructs are being quantified by $\theta$?
- It was challenging to understand how each component of the TestAgent framework depicted in Figure 2 was studied in the evaluation. It seemed like there were many moving parts and was unclear whether the entire framework was being evaluated or just components. Ideally, the evaluation conducted in Section 3 would clearly ablate different individual components. For instance, it is not clear if the dynamic question selection, autonomous feedback, and anomaly management modules were evaluated independently or only as a combined system. The lack of ablation studies makes it difficult to assess the contribution of each component.
- There was a general lack of details in the results in terms of methodology. In Section 3.1, the authors say “We fine-tuned the ChatGLM2- 6B (GLM et al., 2024) series using comprehensive expert diagnosis reports and synthetic datasets as fine-tuning data.” This type of language glosses over a lot of the details about what the fine-tuning process looked like, what exact datasets were used, and how synthetic datasets were generated. Another example is in L264, where the authors say “we train a classifier” without further details. What is the architecture of the classifier? What is the input and output of the classifier? What loss function was used? These details are crucial for reproducibility.
- The experimental setup could also be described in much more detail. The authors describe using student data in simulation experiments. How much data were there in each dataset? Where was this data obtained from? These datasets seem to be sourced from very different domains. Section 3.7 needs to be significantly elaborated on. Were the volunteers trained to perform these types of assessments? What kinds of instructions were they given? What version of TestAgent was used? Please provide more of these details in the main text and Appendix. The description of the human study lacks crucial details about the experimental protocol, participant instructions, and the specific version of TestAgent used.
- There seem to be some issues regarding the claims of effectiveness. In Table 1, the authors say that “the bold text indicates statistically significant superiority (p-value ≤ 0.01) over the best baseline”. How is this possible given some of the results in the table? For example, in Table 1 (a) MAAT has an AUC@50 of 65.12+/-1.48 and TestAgent+KLI an AUC@50 of 65.12+/-1.48, and yet only the latter is bolded. Please provide more detail on what statistical tests were conducted.

### Questions
Please address the specific questions raised in the weaknesses section.

### Soundness
2

### Presentation
1

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
The paper, presents TestAgent, a novel system that leverages large language models to improve the process of adaptive testing. Traditional adaptive testing methods, widely used in standardized assessments, face certain limitations, such as fixed-answer question formats, susceptibility to noisy data, and limited personalization in feedback. TestAgent addresses these challenges by employing a dynamic, conversational approach that allows the testing process to adjust in real-time based on each examinee’s responses. This design enables TestAgent to reduce the number of questions needed for precise assessment, achieving approximately 20% fewer questions while maintaining accuracy.

One of TestAgent's primary innovations lies in its ability to adapt questions interactively through natural language, making the testing experience more human-like and less mechanized. Additionally, TestAgent includes mechanisms for autonomous feedback and anomaly management, which detect inconsistencies in responses—such as guessing or ambiguous answers—and address them to enhance assessment reliability. The system also generates comprehensive diagnostic reports, providing examinees with detailed insights into their abilities and areas for improvement. In extensive testing across multiple domains, including educational, personality, and mental health assessments, TestAgent demonstrates significant performance gains in both accuracy and efficiency over traditional methods. By integrating LLMs into adaptive testing, TestAgent represents a significant step forward in creating personalized, conversational assessments that cater to individual user needs and provide a more interactive and engaging testing experience.

### Strengths
Originality: One of the paper’s most compelling strengths is its originality. By integrating large language models (LLMs) into the adaptive testing process, it introduces a novel application that creatively merges advanced language modeling with educational and psychological assessment. This approach innovates beyond traditional methods by offering a conversational, interactive experience in adaptive testing, thereby removing several limitations of rigid, fixed-question formats. The introduction of modules for autonomous feedback and anomaly management is particularly inventive, as it enhances the reliability of adaptive assessments through a system that actively manages ambiguous or inconsistent responses, a feature uncommon in prior adaptive testing approaches.

Quality: The research methodology is rigorous and well-executed, strengthening the quality of the paper’s contributions. The authors conducted extensive experiments on multiple datasets spanning educational, personality, and mental health domains, which demonstrate the model’s versatility and effectiveness. The choice of datasets and comparison with established baseline methods, such as random selection, FSI, KLI, and MAAT, ensure that the results are robust and credible. The use of metrics such as accuracy and area under the curve provides a clear quantitative evaluation of the model’s improvements, while the case studies highlight its practical applications.

Clarity: The paper is generally well-written and logically structured, making its technical content accessible to a broad audience. The problem formulation and objectives are clearly stated, and the contextual background effectively situates TestAgent within the larger field of adaptive testing. Figures and diagrams, such as the overall framework and case study examples, enhance the paper’s readability by visually illustrating the TestAgent’s processes and user interactions. Minor improvements in some sections, such as providing additional details on failure modes, could further enhance clarity, but overall, the writing style and organization serve the paper well.

Significance: The significance of this work is substantial, as it demonstrates how LLMs can enhance adaptive testing, an area of growing importance in personalized education, psychological evaluation, and beyond. By making assessments more interactive and adaptive, TestAgent aligns well with current trends toward personalized AI-driven experiences. The findings have meaningful implications for expanding the applications of LLMs beyond text generation, underscoring the broader potential of AI to enhance human-centered assessment tools. The results show a marked improvement in testing efficiency and accuracy, which could inspire further research and application in various fields, from educational technology to mental health diagnostics. This contribution is particularly relevant to the ICLR community, given its focus on advancements in machine learning and AI applications.

### Weaknesses
Although the paper demonstrates promising results, the experiments rely heavily on synthetic or simulated data to train and evaluate TestAgent. While this is a practical approach for initial testing, it limits the generalizability and applicability of the results to real-world scenarios, where user responses may be less predictable and more varied. Incorporating real-world data from actual assessments, such as real educational tests or personality assessments, could better validate the model’s effectiveness and adaptability. Additionally, discussing any potential discrepancies observed between synthetic and real data could strengthen the understanding of the model’s applicability and limitations in diverse user populations. The paper touches on the presence of errors, such as hallucinations and redundant answers, but it does not thoroughly analyze these issues or quantify their impact on the assessment quality. A deeper exploration of error types and their frequencies could reveal potential failure modes, helping to identify specific limitations or areas where the model struggles. For example, if hallucination errors frequently occur with specific question types, that insight could inform future improvements in the question generation or feedback mechanisms. Adding a robust error analysis, such as categorizing types of errors and discussing mitigation strategies, would provide a clearer understanding of the model’s robustness and improve the transparency of the results.

The paper lacks a discussion on the scalability of TestAgent, particularly when deployed at scale in real-world applications with a large number of test-takers. Given the computational requirements of LLMs, it’s likely that TestAgent requires significant processing power, which may limit its feasibility for institutions with resource constraints. Addressing this issue by either testing the system under constrained environments or proposing strategies to reduce computational load, such as distillation or pruning methods, could enhance its practical value. Discussing trade-offs between performance and efficiency in such settings would provide a more balanced view of the model’s strengths and limitations.

Although the impact statement briefly acknowledges fairness as a future area of research, it does not address potential biases that could arise from using LLMs in adaptive testing. Given that these models might reflect biases present in their training data, it is essential to examine if TestAgent’s question selection or feedback mechanisms favor certain groups or respond inconsistently across diverse demographic groups. Adding an initial analysis of bias or fairness, even at a high level, could demonstrate a commitment to addressing ethical concerns and provide actionable insights for future iterations. Testing TestAgent with users from various backgrounds and examining response patterns could serve as an important step toward ensuring fairness.

While the paper includes user evaluations of TestAgent’s performance, a more detailed comparative analysis of the user experience against traditional testing methods would add value. For example, analyzing user engagement, perceived transparency, and satisfaction with diagnostic feedback compared to conventional adaptive testing methods could highlight specific advantages and shortcomings. Additionally, tracking any learning curve or adaptation period required by users unfamiliar with conversational assessment formats could offer insights into usability and acceptance. Including more qualitative feedback from users, such as perceived accuracy or the helpfulness of the diagnostic report, would provide a holistic view of TestAgent’s effectiveness.

### Questions
Question: How does the model perform when evaluated on real-world data? Are there specific reasons for relying solely on synthetic data in the experiments?
Suggestion: Including experiments or case studies with real-world assessment data would strengthen the evidence base. If access to such data is restricted, discussing potential limitations that may arise when applying TestAgent to real users would be helpful.

Question: Could the authors provide a breakdown of the types of errors observed in more detail? For example, what percentage of errors were due to hallucinations, misinterpretations, or other issues?
Suggestion: A thorough analysis of error types, including quantification and discussion of the impact on assessment quality, would improve transparency and demonstrate robustness. Could specific adjustments in the feedback or anomaly modules mitigate these errors?


Question: Have the authors considered potential biases that might arise in the question selection or response evaluation mechanisms? Are there steps in place to identify or mitigate these biases?
Suggestion: Adding a preliminary analysis of fairness or bias, even if high-level, could address concerns about the model’s consistent behavior across diverse demographic groups. It would also provide insight into the challenges and plans for ensuring equity in assessments.


Question: Can the authors elaborate on the computational requirements for running TestAgent, especially in resource-constrained environments?
Suggestion: A discussion on scalability, including potential strategies to reduce computational load provide practical insights for broader applicability.



Question: How does TestAgent compare with traditional adaptive testing methods in terms of user engagement and satisfaction with the testing process?
Suggestion: Incorporating a more detailed comparative analysis on user experience, perhaps by analyzing user satisfaction or perceived accuracy against conventional methods, could highlight TestAgent’s unique benefits. Any qualitative feedback on the diagnostic reports would also be informative.



Question: How effectively does the Autonomous Feedback Mechanism handle ambiguous responses in practice, and are there thresholds for when a response is deemed too ambiguous?
Suggestion: Providing examples of ambiguous responses and explaining how the feedback mechanism resolves them would clarify its practical effectiveness. If there are predefined thresholds for ambiguity, detailing these would improve understanding of the system’s robustness.

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
2

### Summary
Even though I’m not an expert in the field of Knowledge Tracing, I have to say, the amount of work and dedication that went into this research is really impressive. This paper introduces a model called CUFF-KT, which tackles a pretty big problem in Knowledge Tracing known as Real-time Learning Pattern Adjustment (RLPA). Why is this important? Well, learners’ knowledge states are constantly changing, and most existing models just can’t keep up with those shifts. CUFF-KT uses a controller and a generator module to adapt to these changes in a flexible and quick way, without the need for fine-tuning. This not only helps avoid overfitting but also significantly reduces time costs. From the experiments, it’s clear that CUFF-KT performs better than traditional methods on several datasets, making it a very promising solution for real-world applications.

### Strengths
One of the most remarkable aspects of this paper is its introduction of a new task, RLPA, which fills a gap in the field of Knowledge Tracing. Most traditional models assume that training and test data distributions remain the same, but CUFF-KT challenges that assumption with a much more flexible approach. This isn’t just a refinement of existing models—it’s a fresh way of addressing a real-world problem. Specifically, it handles learners’ constantly evolving learning patterns without needing to retrain the model frequently, which is a major leap forward.

The quality of this research is also worth noting. The experiments are carefully designed, and the datasets used cover both classic and cutting-edge examples. CUFF-KT improves the AUC (a key performance metric) by around 7% across multiple datasets, which is a significant improvement. The authors have done a fantastic job of demonstrating that CUFF-KT is not just a theoretical concept but a practical solution that actually works.

Even though the subject matter can get pretty technical, the paper is written clearly and walks the reader through the challenges and how CUFF-KT solves them. It flows smoothly from problem statement to solution and finally to experimental validation. This structure makes it accessible even to those who may not be deeply familiar with the field of Knowledge Tracing.

In terms of impact, CUFF-KT has the potential to make a big difference in how personalized learning systems are developed. By enhancing models’ ability to adapt to real-time changes in learning patterns, this research opens the door to smarter, more responsive educational technologies. It’s especially relevant for Intelligent Tutoring Systems, where individual learning paths need to be adjusted frequently. This model has wide-ranging applications and potential.

### Weaknesses
In the final step of the framework, expert analysis is still required. This feels a bit contradictory to the goal of improving automation. Since you're already using LLMs, why not go a step further and design an evaluation agent to replace or supplement the expert analysis? This could boost efficiency and reduce dependence on experts.

While the framework diagram is clear, I think it could be made even more detailed. For example, showing the flow of data between different modules, including the specific data structures being passed, could make it easier to understand how the system operates, especially for readers unfamiliar with the field. This would help clarify the interaction between the question generation, cognitive diagnosis, and adaptive question selection modules.

The paper discusses two key components of TestAgent: adaptive question selection and cognitive diagnosis. I think an ablation study would be helpful to evaluate the individual contributions of these components. It could also be interesting to see what happens if human experts take over one of these components, providing insight into human-machine collaboration. For example, how would the system's performance change if a human expert selected questions based on the current diagnosis, or if a human expert provided the diagnosis based on the responses?

The appendix gives some examples of the tests, but it doesn’t show the full prompts sent to the agent. For an LLM-based system, the design of the prompts is crucial, as it defines the task and the agent's role. I suggest the authors provide more detail about how these prompts are structured, including the specific instructions, constraints, and few-shot examples used, to give a clearer picture of how the system operates. This is particularly important for reproducibility and for understanding the agent's behavior in different testing scenarios.

### Questions
1.Could CUFF-KT’s adaptive framework be applied to other fields, such as personalized recommendation systems or adaptive testing platforms? If so, what changes would be necessary to make it work effectively in these areas?

2.How does CUFF-KT handle very large and complex datasets with highly diverse learning behaviors? Does its efficiency drop when dealing with such cases, and are there any ways to further optimize it for more dynamic or unpredictable learning environments?

3.The paper mentions that CUFF-KT doesn’t require fine-tuning, which is a great feature. Could you provide more details on how the model manages to avoid overfitting while still maintaining high accuracy without needing retraining? A bit more clarity on this point would be valuable, especially for readers who are curious about the technical details behind the scenes.

### Soundness
3

### Presentation
3

### Contribution
3
