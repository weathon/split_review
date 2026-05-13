# Cuff-KT: Tackling Learners' Real-time Learning Pattern Adjustment via Tuning-Free Knowledge State-Guided Model Updating

- Decision: Reject
- Scores: 3, 5, 5, 6

## Abstract
Knowledge Tracing (KT) is a core component of Intelligent Tutoring Systems, modeling learners' knowledge state to predict future performance and provide personalized learning support. Current KT models simply assume that training data and test data follow the same distribution. However, this is challenged by the continuous changes in learners' patterns. In reality, learners' patterns change irregularly at different stages ($e.g.$, different semesters) due to factors like cognitive fatigue and external stress. Additionally, there are significant differences in the patterns of learners from various groups ($e.g.$, different classes), influenced by social cognition, resource optimization, etc. We refer to these distribution changes at different stages and from different groups as intra-learner shift and inter-learner shift, respectively---a task introduced, which we refer to as Real-time Learning Pattern Adjustment (RLPA). Existing KT models, when faced with RLPA, lack sufficient adaptability, because they fail to timely account for the dynamic nature of different learners' evolving learning patterns. Current strategies for enhancing adaptability rely on retraining, which leads to significant overfitting and high time cost problem. To address this, we propose Cuff-KT, comprising a controller and a generator. The controller assigns value scores to learners, while the generator generates personalized parameters for selected learners. Cuff-KT adapts to distribution changes fast and flexibly without fine-tuning. Experiments on one classic and two latest datasets demonstrate that Cuff-KT significantly improves current KT models' performance under intra- and inter-learner shifts, with an average relative increase of 7\% on AUC, effectively tackling RLPA. Our code and datasets are available at https://anonymous.4open.science/r/Cuff-KT.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces the concept of Real-time Learning Pattern Adjustment (RLPA), which highlights the intra-learner and inter-learner shifts that affect learners’ knowledge states due to factors like cognitive fatigue and external stress. To address the proposed challenge, the authors propose a novel method called Cuff-KT, which consists of a controller that identifies learners with dramatic changes in their knowledge state distribution and a generator that produces personalized parameters without requiring retraining. This approach allows for fast and flexible adaptation to distribution changes, effectively improving KT models' performance.

### Strengths
The study has shown improvement on different KT base models and some finetune methods on a wide range of datasets. Furthermore, several figures are drawn in this paper with bright colors and clear layouts.

### Weaknesses
1.	Some mistakes regarding presentation:

a.	In Line 251 $ZPO^j$ should be $ZPD^j$ (The same is true in the source code `train.py`);

b.	In Line 328, $k$ indicates the number of samples, but it has been defined in Line 265 (time-step $k$);

c.	The use of notation in the paper is confusing, lacking a clear distinction between matrices, vectors and scalars, e.g., Line 274 and Line 313.

d.	The counter of equations does not work well. For example, there are two Eq. (4) in page 5.

e.	The citation format is inconsistent; for example, the conference paper lacks the address.

2.	The task RLPA seems like the specification of the distribution shift in time series forecasting in knowledge tracing scenarios [1]. It’s believed that temporal distribution shifts are quite common in time series forecasting and has many solutions. However, the paper does not mention anyone in related work or make any of them compared with the proposed method. 

3.	Line 204 is unrelated to the proposed RLPA task. Minimizing this KL divergence is the same as the BCE loss in Line 328, which is the typical KT task loss. This formula doesn't hold any practical significance here.

4.	The paper doesn’t clearly explain the experimental setup. For example, it’s hard to find a straightforward description of how datasets are divided in settings of inter-learner and intra-learner respectively; you have to look at the code to figure it out.

References:

[1] Fan et al. Dish-TS: A General Paradigm for Alleviating Distribution Shift in Time Series Forecasting. In _Proceedings of the 37th AAAI Conference on Artificial Intelligence_, Washington, DC.

### Questions
In addition to the previously mentioned weaknesses, there are some other questions:

1.	Is it really necessary to fine-tune to solve this problem? In addition to the framework mentioned, it should also compare their framework with some SOTA KT methods to see if their approach improves upon the basic methods more than the SOTA methods do.

2.	Why does the source code include the LoRA method, yet this is not used as a baseline in experiments?

3.	Why is the AUC on xes3g5m in the setting of intra-learner less than that in the inter-learner? Since AUC on assist15 and comp in the setting of intra-learner is greater than that in the inter-learner.

4.	In Line 244, what is the rationale for choosing $k/2$? Why isn't the $\sum_{i=1}^k1$ simply written as $k$ here?

5.	A more detailed explanation of the specific educational implications of the formulas in lines 293-298 could be provided.

I will raise my score if these questions are addressed.

### Soundness
3

### Presentation
2

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
This work proposes a novel method  called Controllable, tUning- free, Fast, and Flexible Knowledge Tracing (Cuff-KT) to address intra- and inter-learner shifts in student performance prediction. Cuff-KT has two components, a controller and generator mechanism, to learn a model parameter generator specific to the current stage or group and generate updating personalized parameters for valuable learners (e.g., those showing significant progress or regression).

### Strengths
I acknowledge the problem setting in this paper is unexplored, regarding the performance distribution shift in educational datasets coming from both students' progress and the online platform's selection mechanism. 
The authors also effectively present the problem and motivation, offering a clear and accessible read. I appreciate that Cuff-KT shows a first step to bring this problem into the public, instead of only relying on heavy neural networks and large data to chase the SOTA performance. 

Regarding the method, including the controller and the generator, which I also find them very interesting. Though the details of each part are a bit confusing to me (see weaknesses), figure 3 effectively visualizes the overall Cuff-KT pipeline

### Weaknesses
The literature review omits recent models like QIKT, SimpleKT, and PSIKT. Including these would clarify Cuff-KT’s positioning. Additionally, the rationale for selecting the three evaluation baselines needs more explanation.

The clarifications of the experiment setup and details of the methodology need improvement, but do correct me if I am missing anything here:

1.	In lines 226 and 431, the authors mention “e.g., KL-divergence,” but it is unclear if other distance measures were considered. It would also be helpful to know how the distribution over embeddings was approximated—was it, for instance, fitted to a Gaussian?
2.	In the controller setting, is there any specific reason that the authors chose to compare step $k$ and intermediate time-step $\frac{k}{2}$, i.e., why not using a sliding window setting? Theoretically, as the time step $k$ goes up, the discrepency between the two distributions will not decrease. This means the $\mathrm{KL}^j$ in Eq.4 will always become larger. Does the model prioritize students with longer learning histories, thereby increasing their likelihood of selection?
3.	In Sec. 3.2.2, I would need much more clarifications so that I can comment on this part. In line 265, $c_i$ and $r_i$ are input for question difficulty and learner ability. Why do authors choose $c_i$ as the input or it is a typo? This question applies to all of the question/concept notations in this section, e.g., “embedding the questions $c_{1: k}$”. I will try to comment on the soundness of generator again after the authors clarify this section. Meanwhile, how do authors embed the time information, i.e., what is $t_{1:k}$ in Eq. 5?
4.	The experiment training and validation needs more clarifications. In lines 368-370, the authors say the historical interactions are split into training, validation, and test sets based on the timestamps and groups. I am not clear how inter- and intra- evaluations are done and how the training and test work, could the authors provide better explanations (more details can come in the appendix if it exceeds page limit)?
5.	Do the authors provide the effectiveness of the controller? How do the performance change if you remove the controller at all, i.e., the model will generate the parameters for every student? I also wonder the statistics of the student chosen by the controller, how many students are chosen in general and what is the correlation between the chosen students and their interaction length? As I wonder in question 2, if the length plays a dominant role (as the authors show in Fig. 7), what else is determining the chosen probability intuitively?

### Questions
I would appreciate the authors could answer my questions and add additional experiments/clarifications in the manuscript I proposed in the weakness.

I need further clarification on the remaining questions:

1.	In Eq.2, is the time index $u$ not the actual timestamp but rather the $u$-th interaction of  student $s$. Why did the authors choose to compare students based on their individual learning progress instead of at an arbitrary time horizon? Was this choice made for engineering or implementation convenience?
2.	In Sec. 4.2, I appreciate the inclusion of anomaly detection. However, where does the ground truth for anomaly points in the student KT datasets come from? Do these datasets provide these points? 
3.	I suggest the authors revise the presentation of Figures 5 and 8. The overlapping purple colors create confusion; a standard bar plot would improve clarity significantly.

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
This paper presents the CUFF-KT, which tackles real-time learning pattern adjustment in knowledge tracing by leveraging a tuning-free knowledge state-guided model update approach. CUFF-KT comprises controller and generator modules, capable of generating personalized parameters to adapt quickly to changes in learner distributions. Experiments demonstrate that CUFF-KT significantly improves model performance under various learning pattern shifts.

### Strengths
1. This paper use a motivation study to identify a new task called Real-time Learning Pattern Adjustment  which aims at capturing the dynamic nature of different learners’ evolving learning patterns.
2. The proposed Cuff-KT appears to address the issues effectively compared with the selected baselines, as indicated by the experimental results.
3. The structure and framework figure of the paper is clear and easy to follow, making it accessible for readers. However, some formulas are somewhat complex and may benefit from further clarification.

### Weaknesses
1. **My biggest concern is why the paper introduces the topic from the perspective of distribution shift and compares with anomaly detection methods.**  How are these two concepts related? My understanding is that it’s one of the causes of distribution shift. The term "anomaly detection" first appears in line 377. What constitutes an anomaly in knowledge tracing? After reading the motivation study, I speculate that anomaly detection in knowledge tracing might refer to changes in students' accuracy rates. In summary, the relationship of two concepts could benefit from more explanation and clarification in the introduction and related work.
2. If this is indeed anomaly detection, then I believe the authors should compare their method with HD-KT[1] to validate its effectiveness.
3. The author cited numerous papers in the related work, such as iAKT [2], which address handling different distributions. Why weren’t these methods included for comparison?

[1] Ma, Haiping, et al. "HD-KT: Advancing Robust Knowledge Tracing via Anomalous Learning Interaction Detection." Proceedings of the ACM on Web Conference 2024. 2024.

[2] Wong, Cheryl Sze Yin, et al. "Incremental context aware attentive knowledge tracing." ICASSP 2022

### Questions
1. **Clarification on Distribution Shift and Anomaly Detection**: The paper introduces distribution shift and compares it to anomaly detection methods, but the relationship between these concepts isn’t fully explained. Further clarification is needed on how anomaly detection contributes to or causes distribution shift, especially since anomaly detection first appears in line 377. A clearer explanation in the introduction and related work would help readers understand how "anomaly" is defined within the context of knowledge tracing.

2. **Comparison with HD-KT**: If the method is indeed related to anomaly detection, a comparison with HD-KT, which also addresses anomalous learning interactions, would strengthen the validation of the proposed method.

3. **Comparison with Distribution-Handling Methods like iAKT**: While the authors reference several methods in the related work section that handle different distributions (e.g., iAKT), these methods are not included in the experimental comparisons. A comparison with these approaches would provide a more comprehensive evaluation of the method's effectiveness.

### Soundness
4

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
2

### Summary
As an expert in large language models (LLMs), I must admit I’m not very familiar with cognitive diagnosis. So, my review will mostly focus on the LLM aspects. This paper introduces TestAgent, an adaptive testing agent based on LLMs, and honestly, the system has great potential. It conducts adaptive testing through interactive dialogues, which I think is a very cool idea. It helps solve some of the issues in traditional adaptive testing, like rigid question formats, noise in the data affecting accuracy, and overly simple output. By combining adaptive question selection and cognitive diagnosis, TestAgent dynamically selects personalized questions based on performance, identifies anomalies, and provides detailed diagnostic reports. What's even better is that it reduced the number of test questions by about 20% in several domains, such as psychological and educational testing, significantly improving testing efficiency.

### Strengths
Originality: What impressed me the most is the combination of LLMs with adaptive testing. This is a fresh approach that breaks away from traditional, static testing, making the process much more flexible and interactive. The ability to generate personalized questions using LLMs really improves the overall testing experience.

Quality: From the experimental results, TestAgent shows excellent performance in multiple fields. Reducing the number of test questions by 20% without sacrificing accuracy is incredibly valuable in real-world applications, saving time and maintaining reliability.

Clarity: The paper is well-structured, and I particularly appreciated Figure 2, which clearly shows how the entire system works. Even readers who aren’t familiar with this area can easily understand the role of each module.

Significance: In terms of practical applications, TestAgent has a lot of potential. Whether it's in education or mental health, personalized assessments and real-time feedback are crucial. A system that can dynamically adapt to user needs could have a big impact.

### Weaknesses
In the final step of the framework, expert analysis is still required. This feels a bit contradictory to the goal of improving automation. Since you're already using LLMs, why not go a step further and design an evaluation agent to replace or supplement the expert analysis? This could boost efficiency and reduce dependence on experts.

While the framework diagram is clear, I think it could be made even more detailed. For example, showing the flow of data between different modules could make it easier to understand how the system operates, especially for readers unfamiliar with the field.

The paper discusses two key components of TestAgent: adaptive question selection and cognitive diagnosis. I think an ablation study would be helpful to evaluate the individual contributions of these components. It could also be interesting to see what happens if human experts take over one of these components, providing insight into human-machine collaboration.

The appendix gives some examples of the tests, but it doesn’t show the full prompts sent to the agent. For an LLM-based system, the design of the prompts is crucial, as it defines the task and the agent's role. I suggest the authors provide more detail about how these prompts are structured to give a clearer picture of how the system operates.

### Questions
In the final step of expert analysis, could an evaluation agent replace the expert? If so, how would this change the system’s automation and efficiency? Has this alternative been considered?

Could you provide more detail about the prompts used to define the agent’s tasks? How do these prompts affect the agent’s behavior, especially in more complex testing scenarios?

Have you considered conducting an ablation study to test the individual contributions of the adaptive question selection and cognitive diagnosis modules? How would the system perform if one of these components was replaced by expert intervention?

### Soundness
4

### Presentation
3

### Contribution
3
