# Students Rather Than Experts: A New AI for Education Pipeline to Model More Human-like and Personalised Early Adolescences

- Decision: Reject
- Scores: 3, 6, 5, 6

## Abstract
The capabilities of large language models (LLMs) have been applied in expert systems across various domains, providing new opportunities for AI in Education (AI4Education). Educational interactions involve a cyclical exchange between teachers and students. Current research predominantly focuses on using LLMs to simulate teachers, leveraging their expertise to enhance student learning outcomes. However, the simulation of students, which could improve teachers' instructional skills, has received insufficient attention due to the challenges of modeling and evaluating virtual students. This research poses the question: ``\textit{Can LLMs be utilized to develop virtual student agents that mimic human-like performance and individual variability?}" Unlike expert systems focusing on knowledge delivery, virtual students must replicate learning difficulties, emotional responses, and linguistic uncertainties. These traits present significant challenges in both modeling and evaluation. To address these issues, this study focuses on language learning as a context for modeling virtual student agents. We propose a novel AI4Education framework, termed \textbf{SOE} (\textbf{S}cene - \textbf{O}bject - \textbf{E}valuation), to systematically construct \textbf{LVSA} (\textbf{L}LM-based \textbf{V}irtual \textbf{S}tudent \textbf{A}gents). By curating a dataset of personalized teacher-student interactions with various personality traits, question types, and learning stages, and fine-tuning LLMs using LoRA, we conduct multi-dimensional evaluation experiments. Specifically, we: (1) develop a theoretical framework for generating LVSA; (2) integrate human subjective evaluation metrics into GPT-4 assessments, demonstrating a strong correlation between human evaluators and GPT-4 in judging LVSA authenticity; and (3) validate that LLMs can generate human-like, personalized virtual student agents in educational contexts, laying a foundation for future applications in pre-service teacher training and multi-agent simulation environments.
More related resources will be released at:  \href{https://marsgemini.io/SOE-LVSA/}{https://marsgemini.io/SOE-LVSA/}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper tries to simulate student behaviors (as opposed to teachers behavior) using LLMs and in order to do that, they have proposed SOE (Scene-Object-Evaluation) framework. They evaluate these virtual students using multi-dimensional experiments.
The paper has three contributions: 
1) A theoretical framework for LVSA
2) The integration of human subjective evaluation metrics into GPT-4
3) An empirical demonstration that virtual student agents can closely emulate real student behaviors

### Strengths
- Applying virtual students for teacher training can be potentially impactful.
- Paper is easy to follow

### Weaknesses
 - Reliance on subjective metrics and GPT-4 assessments could introduce biases. Personality-based biases (relying on the Big Five traits -> lead to stereotypical behaviors) and cultural biases (focusing on Chinese students could limit generalizability).
Use a more diverse range of evaluators. 

- Limited realism. Not supporting multimodal inputs limits its usefulness. Incorporating visual and audio elements, at a minimum, could better reflect real-world classroom dynamics.
Real classroom settings often rely on visual and auditory cues.

- Needs more varied context. The model should have the capability to simulate more subjects like math and science. This would allow for a  more relevant model.
The need for a model that is capable of advanced reasoning and interpretation.

### Questions
Some important questions could be how virtual students could be validated in settings beyond junior high language tasks? How might the model be modified to incorporate multimodal inputs? What steps are being taken to address biases that might occur in the evaluations? Did the authors explore additional evaluation metrics? Could the authors elaborate on the ethical implications of simulating student behaviors (data privacy could be a concern)?

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
The paper introduces a novel AI framework, the "Scene-Object-Evaluation" (SOE) pipeline, designed to model Large Language Model-based Virtual Student Agents (LVSA) that mimic the behaviors and personalities of early adolescent students in educational settings. Unlike previous work that uses large language models (LLMs) to simulate expert teaching roles, this study focuses on creating realistic, student-like agents that reflect common learning challenges, emotional reactions, and personality differences.

The SOE pipeline operates in three stages: Scene, which defines the educational scenarios and content; Object, which constructs virtual student agents with distinct personality traits through LoRA fine-tuning; and Evaluation, which assesses these agents' performance using human and GPT-4 evaluations. The virtual students are evaluated based on traits derived from the Big Five Personality Traits framework to ensure a range of realistic, individualized behaviors. Experiments show that these fine-tuned virtual agents provide human-like and personalized responses, validating their potential to support pre-service teacher training by offering realistic classroom simulations.

This research contributes a new approach to AI4Education, focusing on developing student agents that improve teachers’ instructional skills through realistic interactions, and lays groundwork for future applications in teacher training and multi-agent simulations.

### Strengths
This paper brings a high degree of originality by shifting the focus from expert or teacher-oriented AI simulations to student simulations, addressing a significant gap in AI-driven teacher training tools. The introduction of the Scene-Object-Evaluation (SOE) pipeline to model Large Language Model-based Virtual Student Agents (LVSA) represents a creative approach to personalized student simulation, providing an adaptable framework that mirrors the complexity of real students. Using the Big Five Personality Traits for developing distinct virtual student personalities adds further novelty, offering a method for producing varied and realistic student responses that go beyond standard, pre-scripted models.

The research methodology is robust, leveraging the SOE pipeline to guide each stage of student agent construction. The use of LoRA fine-tuning to adapt the LLMs to personality-based response styles is well-executed, supported by a well-defined dataset and clear criteria for generating realistic dialogues. The authors conduct subjective evaluations through human raters and GPT-4, lending credibility to the LVSA models’ authenticity in simulating student behaviors. This multi-dimensional evaluation demonstrates thoughtful experimentation, allowing for both quantitative and qualitative assessments of the LVSA’s effectiveness. The use of the Big Five traits adds psychological rigor, enhancing the methodological depth and grounding the work in established personality theory.

The paper is generally clear in its presentation, with each step of the SOE pipeline outlined in a logical and accessible manner. Figures, particularly the pipeline overview, provide helpful visual support, clarifying the process of constructing and evaluating virtual student agents. The experimental setup, while complex, is conveyed effectively, making it easier for readers to understand the key steps and outcomes. However, more detailed examples of LVSA responses across personality types could further improve the clarity and transparency of the results. Expanding on specific evaluation metrics and providing examples of dialogue interactions for different personality types would also enhance readability.

The significance of this work is substantial, as it addresses an important gap in pre-service teacher training by providing a tool for realistic, student-like simulations. In traditional teacher training, access to diverse student interactions is often limited, and this work offers a scalable solution to that problem. The LVSA model provides a unique contribution by capturing the variability of student responses and behaviors, allowing teachers to practice and adapt to different learning personalities and styles. By simulating more realistic classroom scenarios, the LVSA approach has the potential to improve teacher preparedness, adaptability, and effectiveness. These contributions align well with the ICLR community’s interest in novel applications of AI, particularly in education and social simulation, and could stimulate further research into AI-driven, personalized learning simulations.

### Weaknesses
Issue: The evaluation primarily relies on subjective assessments from human raters and comparisons with GPT-4, which introduces variability in interpretation and limits reproducibility.
Suggestion: Including additional objective metrics—such as measuring linguistic coherence, response diversity, or sentiment alignment—could strengthen the evaluation process and provide quantitative insights into LVSA’s effectiveness. Moreover, using established psychometric tools to assess the authenticity of the personality-based responses could enhance credibility. Adding these metrics would improve the benchmark’s robustness and offer more reproducible, quantitative insights into model performance.


Issue: The evaluation primarily relies on subjective assessments from human raters and comparisons with GPT-4, which introduces variability in interpretation and limits reproducibility.
Suggestion: Including additional objective metrics—such as measuring linguistic coherence, response diversity, or sentiment alignment—could strengthen the evaluation process and provide quantitative insights into LVSA’s effectiveness. Moreover, using established psychometric tools to assess the authenticity of the personality-based responses could enhance credibility. Adding these metrics would improve the benchmark’s robustness and offer more reproducible, quantitative insights into model performance.


Issue: The paper lacks detailed examples of LVSA responses across different personality types, making it challenging to assess the realism and nuances of virtual student interactions. A deeper qualitative analysis of the generated responses could reveal specific strengths and limitations in simulating various personality traits.
Suggestion: Adding representative examples of LVSA responses across personality traits, question types, and learning stages would clarify how the model adapts to different scenarios. A qualitative analysis of these responses could provide actionable insights into areas where the model succeeds and where it may struggle to simulate certain personalities. This addition would also make the results more transparent and accessible to readers interested in the specifics of the student interactions.



Issue: The paper notes difficulties in modeling low-conscientiousness (LC) virtual students and instances of hallucination, where generated responses lack coherence. However, these challenges are not fully explored, and there is little discussion on specific mitigation strategies.
Suggestion: Including a more comprehensive analysis of failure cases, especially regarding LC personality traits, would improve understanding of the model’s limitations. Discussing methods to mitigate hallucinations, such as incorporating stricter training constraints or filtering responses, could add value to the paper and inform future improvements. Identifying potential approaches to handle “undesirable” traits like low conscientiousness could also clarify how LVSA might be adapted for broader educational use.


Issue: The SOE pipeline's adaptability to varying classroom contexts, cultural backgrounds, or different educational levels is not addressed, which may affect its broader applicability and restrict generalization across diverse educational settings.
Suggestion: Discussing the adaptability of the SOE pipeline to various contexts, such as different age groups, subject areas, or cultural backgrounds, would enhance the relevance of the work. Exploring how the model could be fine-tuned or adjusted to reflect different educational environments would increase its generalizability and appeal. Additionally, expanding the fine-tuning dataset to include a wider array of scenarios or educational subjects could improve model robustness across diverse contexts.

### Questions
Question: Beyond human and GPT-4 evaluations, did you consider incorporating objective metrics such as linguistic coherence, response diversity, or sentiment analysis to evaluate the LVSA’s responses?
Suggestion: Adding these metrics would enhance the rigor and reproducibility of the evaluation process. Objective measures could also help reduce variability in subjective assessments and provide additional quantitative insights into the effectiveness of the LVSA.


Question: Do you have plans to test the LVSA in real-world educational settings or with pre-service teachers? If so, what are your anticipated challenges in transitioning from simulation to actual classroom interactions?
Suggestion: Conducting field tests or real-world studies with pre-service teachers interacting with LVSA could provide valuable insights into the model’s practical value and usability. Understanding how LVSA performs in diverse, real-life scenarios would bolster its credibility and relevance for educational applications.


Question: Could you provide specific examples of how LVSA responses differ across personality types, particularly with the Big Five traits? Are there qualitative differences in the way different personality modes handle similar questions or challenges?
Suggestion: Including examples of LVSA responses across a variety of personality traits and educational scenarios would enhance transparency and allow readers to better understand the nuances of the virtual student interactions. This would also make it easier to assess the model’s adaptability and realism in simulating diverse student behaviors.

Question: You mention difficulties with modeling low-conscientiousness traits and hallucination issues. Could you elaborate on the specific challenges faced and any steps taken to mitigate these problems?
Suggestion: Providing a detailed analysis of failure cases, especially in simulating LC traits, would clarify the model’s limitations. Discussing potential strategies to reduce hallucinations (such as response filtering or stricter fine-tuning constraints) would improve the framework’s robustness and help readers understand how LVSA might be improved for complex or nuanced personalities.


Question: How adaptable is the SOE pipeline to different classroom contexts, age groups, or cultural backgrounds? Could it be easily fine-tuned for students in different educational systems or with varying cultural characteristics?
Suggestion: Discussing how the SOE pipeline could be generalized or adjusted to accommodate diverse educational contexts would enhance its broader applicability. Exploring fine-tuning or dataset adjustments that capture different cultural and age-based contexts would clarify how adaptable the LVSA could be in global educational settings.

Question: Have you considered conducting longitudinal studies to assess whether interactions with LVSA lead to measurable improvements in teachers’ skills, particularly in classroom management or personalized instruction?
Suggestion: If feasible, a longitudinal study tracking skill development in pre-service teachers over time would provide a deeper understanding of LVSA’s educational impact. This type of evaluation could offer insights into whether sustained interaction with diverse virtual students has lasting benefits on teachers’ adaptability and instructional skills.

Plans for Scaling and Efficiency Optimization
Question: Given the computational demands of generating varied personality-based responses, do you have plans to optimize the SOE pipeline for efficiency, perhaps through model distillation or response sampling techniques?
Suggestion: Discussing strategies for scaling or optimizing the model’s computational efficiency would improve the framework’s usability for larger educational deployments. Efficiency improvements could also make LVSA more accessible to institutions with limited computational resources.

### Soundness
3

### Presentation
3

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
This work presents an AI4Education framework, termed SOE (Scene - Object - Evaluation), to construct LVSA (LLM-based Virtual Student Agents). It contributes a new Chinese education dataset and evaluates four existing LLMs which are fine-tuned in this dataset in simulating virtual students with specific traits. A Turing test is used to evaluate whether LLMs can generate such human-like virtual students. Specifically, GPT-4 is used for large-scale automatic evaluation and a small group of real humans are recruited for small-scale evaluation.

### Strengths
1. This work presents a LLMs-based agent evaluation pipeline including data preparation, LLM fine-tuning, and virtual student evaluation.

2. A new large dataset is contributed to study the virtual student agents mimicked by LLMs.

3. A comprehensive experiment is conducted to evaluate the performance of student agents powered by LLMs.

4. This paper presents sufficient supplemental materials for the readers to understand the prompts.

5. Overall, it is easy to read and understand this paper, with clear arguments.

### Weaknesses
W1. One of my main concerns is the novelty in model/framework design. The proposed SOE framework looks more like a dataset processing and LLM testing pipeline. However, this is no specific model design or new prompt structure design. The authors simply instruct the LLMs to mimic students with different traits based on the big five rationale. The LLMs used from existing work are directly fine-tuned on a new dataset. There are no unique insights in prompt design or fine-tuning strategies, compared with previous work. Moreover, the incorporation of big five theory for agent personality is also widely utilized in existing work such as [1]. Therefore, this is not a novelty nor contribution.

W2. Another main concern is that I think this work cannot really support its claim in line 532 "resembled real student behavior" and line 533 “simulating realistic student roles”. I agree with line 053 “virtual student agents must replicate a broader range of human behaviors”. But such replication needs labels/ground truth to demonstrate and quantify the accuracy of such replication. A simple Turing test cannot really support that, and lots of existing work has explored LLMs in passing Turing test [2] and a new Turing experiment [3]. That said, Turing test can show that your agent simulation is human-like, but that does not necessarily mean that your agent simulation is realistic among students’ real behaviors, which needs more convincing ground truth for comparison. But this work does not have a real ground truth for comparison.

Specifically, I also do not understand why the five kinds of agents (HN, HA, LO, HE, LC) are combined with real students as the six one together for evaluation in appendix figure A18. Do the authors mean that human evaluators are asked to distinguish one of the six types? I’m confused because at first the authors say that this work aims to simulate student traits. So I thought real students serve as the labels instead of an additional type in addition to the five traits. Such Turing test setting can only show that humans cannot distinguish whether the expressions are from agents or real students. This is not surprising considering existing work showing the performance of LLMs in the Turing test such as [2]. However, it cannot show that such simulation is realistic because there is no ground truth for comparison.

W3. I’m also concerned regarding the limited generalization and evaluation. This work only uses one Chinese dataset from the authors. No public datasets or English datasets are used. It is uncertain whether the performance of this framework can have good generalization.

W4. Moreover, another important concern is the lack of a real baseline. The evaluation simply compares pre-finetuning with post-finetuning. It is not surprising that finetuning in the targeted dataset can result in better performance. But there is not a real baseline to show the unique advantage of the propose SOE framework, compared with existing approaches.

W5. Furthermore, using GPT-4 for automatic evaluation is not convincing. It looks like the authors are using one LLM to evaluate other LLMs’ performance. No ground truth is used for more convincing evaluation. Line 373 mentioned the high inter-coder reliability just proves that the two students have consistent opinions in annotation. But it cannot prove that GPT 4 is a convincing automatic evaluation tool to replace real human annotators to perform automatic evaluation.

W6. In Appendix D.5.3 and figure A18, since GPT4 can “effectively simulate and assess nuanced student behaviors” (from line 4236), why not directly use GPT4 for student trait simulation? Why do you use other LLMs to perform such simulation and use GPT 4 to serve as the evaluator? Furthermore, in line 4244, “GPT-4 and human evaluators was found to be 0.6806, which falls within the range of substantial agreement”. Why 0.6806 is acceptable and why 0.6806 is within the range of substantial agreement? Who defines the agreement? Is there a standard rule for the value range?

W7. I’m really confused about what the evaluation score means in section 5.4. What the score refers to? What does 100% mean in line 416? Does it refer to the accuracy for human evaluators or GPT 4 to distinguish different types of agent traits? Similarly, for different learning stages in line 463 and different question types in line 482, what does the percent % mean? Does it refer to the accuracy or any metrics, to measure what?

W8. Line 478: “These findings suggest that LVSA effectively adapts to different learning stages, offering comprehensive support for pre-service teacher training. Virtual students enable teachers to practice and refine instructional strategies across all teaching phases, enhancing skill development throughout the entire instructional process.” These assertions are over-claimed. If you want to show its effectiveness to help teachers, then you need to conduct a real teaching experiment to show it, which is more convincing. Otherwise, such assertions sound weak.

W9. Line 334: No ethic information (such as IRB approval) about recruiting human participants for evaluation and releasing collected datasets to the public. Potential ethic concerns.

W10. 115 samples are too limited for human evaluation. The number of questions used for human evaluation in Appendix Figure A11 and table A3 is too limited. It is also unclear why you only use 40 samples or 35 samples per setting, which is quite confusing. Why all five fatigue test items come from the real student responses? Why not use 2 items from each group of fine-tuned models, direct inference, and real students?

W11. For section 5.2 human Turing test, simply showing the average results of all human evaluators is not a standard nor convincing approach. A formal statistical analysis such as ANOVA is needed.

### Questions
All questions are listed in the weakness above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
++ I have increased the scores after the clarifications from the Authors.

This paper introduces a novel approach to using Large Language Models (LLMs) for simulating virtual students, instead of the more common focus on AI-driven teacher models. The authors propose a framework called SOE (Scene-Object-Evaluation) for generating LLM-based Virtual Student Agents (LVSA). This framework is applied within educational contexts, particularly for teacher training. The key contributions include:

1.Theoretical Framework: A comprehensive model for constructing LVSA based on personalized teacher-student interaction data.
2.Human and GPT-4 Evaluations: The integration of human subjective evaluation with GPT-4's capabilities to assess the authenticity of virtual student agents.
3.Experimental Validation: Extensive experiments confirm the feasibility of generating human-like, personalized virtual student agents for improving teacher training.

### Strengths
Originality: The paper presents a novel shift from teacher-centric AI systems to virtual student simulations, which can greatly impact teacher training and educational AI systems. By focusing on virtual students, it provides a fresh and creative problem formulation, opening new avenues in AI4Education research.

Quality: The paper demonstrates a well-structured methodology, from developing a dataset of teacher-student interactions to fine-tuning LLMs and validating their outputs with human and GPT-4 evaluations. The theoretical and operational frameworks are well thought out, ensuring rigorous scientific contribution.

### Weaknesses
Limited Real-world Data Application: While the framework is well-developed, the fine-tuning process relies on datasets sourced from controlled environments, which may not fully capture the complexity of real-world classroom dynamics. The use of controlled data may lead to virtual students that do not exhibit the full spectrum of behaviors seen in actual classrooms, such as unexpected questions, varied learning paces, and diverse communication styles. Future work should consider using more diverse and naturalistic data for better generalization.


Evaluation Focus: The evaluation primarily centers on language comprehension and emotional simulation. However, cognitive challenges like problem-solving or more complex reasoning skills, which are critical to student behaviors, are underexplored. The current evaluation does not sufficiently assess the virtual students' ability to handle tasks requiring higher-order thinking, such as critical analysis, synthesis of information, or application of knowledge to novel situations. This may limit the scope of the virtual students' realism in broader educational contexts.

### Questions
Handling Cognitive Diversity: Can the authors expand on how their system handles more complex cognitive behaviors beyond basic language learning? For example, how well can LVSA simulate problem-solving tasks or deal with creative thinking in open-ended questions?

Mitigating LLM Hallucinations: What specific strategies can be employed to minimize hallucinations in virtual student responses? Would incorporating additional real-world classroom data or using more advanced fine-tuning methods help in this regard?

### Soundness
3

### Presentation
2

### Contribution
3
