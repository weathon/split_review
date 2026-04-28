# Inference of Evolving Mental States from Irregular Action Events to Understand Human Behaviors

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 5, 6, 6

## Abstract
Inference of latent human mental processes, such as belief, intention, or desire, is crucial for developing AI with human-like intelligence, enabling more effective and timely collaboration. In this paper, we introduce a versatile encoder-decoder model designed to infer  evolving mental processes based on irregularly observed action events and predict future occurrences. The primary challenges arise from two factors: both actions and mental processes are irregular events, and the observed action data is often limited. To address the irregularity of these events, we leverage a temporal point process model within the encoder-decoder framework, effectively capturing the dynamics of both action and mental events. Additionally, we implement a backtracking mechanism in the decoder to enhance the accuracy of predicting future actions and evolving mental states. To tackle the issue of limited data, our model incorporates logic rules as priors, enabling accurate inferences from just a few observed samples. These logic rules can be refined and updated as needed, providing flexibility to the model. Overall, our approach enhances the understanding of human behavior by predicting when actions will occur and how mental processes evolve. Experiments on both synthetic and real-world datasets demonstrate the strong performance of our model in inferring mental states and predicting future actions, contributing to the development of more human-centric AI systems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposed a model combining rule-based learning approaches with statistical approaches to infer evolving mental states and the resulting action seuquences of human beings. The proposed model is advantageous to predict some irregular action events, which is the severest weakness in statistical approaches that strongly depends on sufficient data collections. The proposed decoder is constituted of ruled-based modules which can provide interpretability to some extent. Furthermore, the proposed backtracking mechanism can detect the hiddenly evolving mental states and thus correct the action predictions. The experimental results demonstrate the effectiveness of the proposed approach.

### Strengths
1. This paper combined the statistical model with the rule-base learning approaches, in addressing human behavior prediction. Although in general this kind of combination has been always a research trend in rule-based learning comminity, it is still an intriguing and original approach to be applied in this research problem. One of prominent reasons is that the incorporation of rules can indeed give some interpretation of human behaviors prediction, especially when data is lacking. In my view, this is no doubt a trend of machine learning research in the future.
2. The description of the proposed approach is detailed, with sufficient descriptions on how each module is modelled. The experimental settings are clear and results are compred with multiple baseline algorithms. The illustration of figures helps understand the virtue of the proposed approach.
3. Although this paper lacks some explanations about why some modules are modelled in specific ways, the general description of the proposed modules have been clearly explained. Also, it has evident motivations and sufficient experimental results. Standing on all these point, the quality of this paper is moderate.
4. The research question studied in this paper is significant. Human behavior prediction is always a fundation in dowstream tasks such as human-Al interaction. Most of existing reserch focused on employing pure statistical models to answer this question. One reason is that statistical machine learning has stood out in contrast to logic-based systems since 1990s, and thus people who are knowledgable in logics are not as many as people who are expertised in statistical machine learning. From this perspective, the incorporation of (temporal) logic-based learning into statistical machine learning implemented in this paper is worth encouraging.

### Weaknesses
1. The paper's writing quality needs improvement. While the motivation and research question are clear, the remainder of the paper appears to be an accumulation of descriptions, lacking a clear logical flow to connect the different sections and paragraphs.

2. Typo in line 158-159: Defome -> Deform

3. Lines 170-171 state that the instantaneous event probability is modeled using the hazard function. However, a more detailed explanation is needed regarding the rationale behind choosing the hazard function. What are the specific advantages of using the hazard function compared to other potential models for this purpose? For instance, how does it handle the dynamic nature of event probabilities over time?

4. In line 179, it is mentioned that once a mental event occurs, the discrete-time survival process resets. However, the connection between this statement and equations (1) and (2) is not immediately obvious. Providing more details on how this reset mechanism is justified by these equations would enhance clarity.

5. The time embedding for the observed action time is defined in equation (4). A clearer explanation of the motivation and reasoning behind this specific formulation is needed. What are the benefits of modeling time in this way, and how does it contribute to the overall approach?

6. The probabilistic model for sampling the mental event type is presented in equation (8). Specifically, what is the rationale behind adding the log probability (\(p_{\{|xi\}}\{|\})) to the collected samples (from \(g_{\{|xi\}}\{|\}))? Are there any theoretical underpinnings or empirical evidence that support this particular formulation?

7. A significant challenge in logic-based learning is constructing logic rule templates. It would be beneficial to have a more in-depth discussion on how the proposed approach addresses situations that are less knowledgeable or unfamiliar to humans. Are there any mechanisms for adapting or expanding the rule set when encountering novel scenarios?

8. The resolution of the discretized time grid likely has a significant impact on the performance of the proposed approach. It would be valuable to include a discussion on potential strategies for determining the optimal value of this hyperparameter. How does the choice of resolution affect the trade-off between accuracy and computational efficiency?

### Questions
Please address t he concerns in weaknesses.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper introduces an encoder-decoder framework that infers latent human mental states (e.g., beliefs, intentions) from irregularly observed action events and predicts future actions. By integrating a temporal point process model with logic rules as priors and a backtracking mechanism, the model improves prediction accuracy and adapts effectively to real-time changes. Its performance is validated through experiments on synthetic and real-world datasets, outperforming existing baselines.

### Strengths
- The research problem is valuable in perception level task and can contribute to practical applications such as autonomous driving
- Thorough experiments reveal promising results

### Weaknesses
 - Limited readability: the paper missed several key points for readers without much related background to understand the task. For example, is the task generative or predictive (i.e., does it generate the action and mental thoughts directly or does it select from an action and mental space); in a high level, how does the backtracking mechanism decide whether to generate/predict a mental state or an action? Instead of explaining a specific step in the mechanism, readers may want to understand the mechanism from the motivation.
- If the model is simply selecting a mental state or an action out of a candidate pool, then the model is not able to intrinsically understand the environment and advanced human perception. Generating and mimicking human behaviors requires the model to process the information from the environment and act like human based on word knowledge and rules, which the proposed framework cannot comprehend as it has not seen it all (i.e., gone through massive pre-training). Therefore, I challenge the "understand" behavior referred in the title.

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The article proposes an encoder-decoder model for inferring human mental states, based on irregular behavioral events to predict future actions. By leveraging temporal point processes and a backtracking mechanism, it captures behavioral dynamics, and introduces logical rules to enhance inference capabilities when data is limited. Experimental results demonstrate that this model outperforms baseline methods in intention inference and prediction accuracy.

### Strengths
The formulation in the article is relatively clear in terms of definitions and inference logic, particularly in the sections on conditional entropy and probabilistic modeling (such as the conditional entropy expression in formula (15)). These formulas effectively capture the temporal relationships between events. 
The experiments in the article are relatively thorough, considering a comprehensive range of comparisons.

### Weaknesses
1. The model's performance is dependent on the quality of the logical rules defined and generated; if the rules are of low quality, it may affect inference results. Specifically, the paper does not discuss the sensitivity of the model to the choice of logical predicates and temporal operators used in the rule templates. The process of selecting these templates is not clearly defined, and it is unclear how the model would perform with suboptimal or noisy rule templates. Furthermore, the paper does not address the potential for overfitting to specific rule templates, which could limit the model's generalization capabilities.
2. The backtracking mechanism may increase computational complexity, and further discussion on its design could be interesting. The paper lacks a detailed analysis of the computational overhead introduced by the backtracking process. It is not clear how the number of backtracking steps affects the overall runtime, and whether this overhead scales with the complexity of the input data or the number of rules. Consider considering a priority filtering mechanism within the model to conduct backtracking checks only on the most relevant events, which could make the approach more intriguing. The current approach appears to treat all events equally during backtracking, which may not be efficient.
3. Currently, the model relies on predefined logical rule templates. While this offers strong initial inference capabilities, it may limit the model's adaptability in complex scenarios. The paper does not explore the model's ability to handle situations where the underlying dynamics deviate from the predefined rule templates. The model's reliance on templates may hinder its ability to discover novel patterns or adapt to new environments where the predefined rules are not applicable.

### Questions
1. If the prediction remains inaccurate after multiple rounds of backtracking, how does the mechanism adjust or avoid getting stuck in an infinite loop?  
2. The paper mentions that the rule generator uses predefined templates and a column generation algorithm to generate logic rules, but the specific process and optimization details are not described. How have the most critical rules for improving model performance been identified?  
3. Logic rules are embedded as prior knowledge to enhance inference capabilities, but do different datasets have different requirements for rules?  
4. Does the performance of the backtracking mechanism vary depending on the embedded logic rules?

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
4

### Summary
The paper introduces an versatile encoder-decoder framework to infer and predict evolving human mental states from irregular action events. By implementing a temporal point process model, the authors handle the irregular nature of both action and mental data. A key enhancement is integrating a backtracking mechanism in the decoder, improving the accuracy of future action and mental state predictions. The model also incorporates logic rules as priors, providing robustness in scenarios with limited data availability.

### Strengths
This paper proposes a novel model for asynchronous action sequence modeling and inferring latent mental events. It utilizes a flexible encoder-decoder architecture incorporating predefined temporal logic rule templates as prior knowledge and introducing a rule generator to refine them. The introduction of the backtracking mechanism improved the stability of the model’s predictions. This method demonstrates promising results in both synthetic and real-world datasets. While the integration of rule-based logic for dynamic prediction adjustment presents an interesting angle, this concept may echo principles already employed in fields like imitation learning, where actions are predicted based on observed sequences and thought cloning that attempts to replicate cognitive processes.

### Weaknesses
W1. Encoder-decoder architectures and the inference of mental states have been explored in adjacent areas such as imitation learning and thought cloning. These methodologies similarly attempt to capture and reproduce complex patterns of behavior or cognitive states based on observed actions or external stimuli. How does the proposed model's use of temporal point processes and rule-based logic distinctly improve upon or differ from similar mechanisms used in imitation learning or thought cloning? Can you provide specific examples or comparative analyses that highlight these differences?

W2. The paper does not discuss the computational demands and scalability of the proposed model, which is crucial for assessing its practical applicability in real-world scenarios.

W3. The model's dependence on manually defined logic rules limits its flexibility and may introduce potential biases, reducing its ability to adapt to new data.

W4. In the experimental section, the authors validated their method's effectiveness on both synthetic and real datasets. Although ER% and MAE provide basic quantitative metrics for model performance, considering more evaluation dimensions and a more detailed experimental design could offer deeper insights when dealing with complex psychological prediction models. Particularly, the method seems very similar to thought cloning, and more evaluation metrics should be considered for real datasets like Hand-Me-That to validate the method's practical effectiveness. Here are some references:

[1] Thought Cloning: Learning to Think while Acting by Imitating Human Thinking

[2] Enhaning Human-AI Collaboration Through Logic-guided reasoning 

[3] Infer Human’s Intentions Before Following Natural Language Instructions

W5. Although the model of mental states and action events is introduced, it lacks a detailed explanation of how sub-goals or mental states affect the generation of action events in long horizon tasks, or how action events feedback influences the prediction of mental states. This missing or unclear interaction could make the model's theory perplexing.

### Questions
Q1. The author mentioned, "A novel backtracking action sampling mechanism iteratively refines predictions, significantly improving responsiveness to real-time fluctuations in human behavior." However, in the decoder (Section 4.2), the column generation algorithm involves frequent rule updates and optimizations, which may lead to high computational costs and execution times, especially when the rule set is large or the data volume is substantial. The backtracking mechanism (Section 4.4) sounds innovative, but repeatedly adjusting previously inferred mental states may also require significant computational resources, particularly in dynamic and changing environments. Therefore, could the authors include a comparison of computational costs in the experimental section to assess how well this mechanism performs in real-time applications?

Q2. In Formula 13, the authors use the Monte Carlo method to estimate expectations, which may introduce bias, especially when the sample size is insufficient. Is there any theoretical or empirical analysis to address this issue?

Q3. In Tables 4 and 7, the authors presented ground truth temporal logic rules and corresponding weights for Syn Data-1 and Syn Data-2. How are the rule weights determined? Are they predefined or calculated? Why are they 0.6 or 0.8, and how do these rule weights impact the results?

Q4. The preliminaries mention the use of DT-RP to model mental states in discrete time, while the generation of action events is simulated in continuous time by TPP. Could the simultaneous use of discrete and continuous time in the model possibly lead to inconsistencies in time scales? How do the methods ensure effective transition and interfacing between these two-time scales?

Q5. Although the model of mental states and action events is introduced, it lacks a detailed explanation of how sub-goals or mental states affect the generation of action events in long horizon tasks, or how action events feedback influences the prediction of mental states. This missing or unclear interaction could make the model's theory perplexing.

Q6. Although self-attention can handle action sequences, its decision-making process is usually not transparent, with poor interpretability. Could techniques like visualization of attention weights be employed to explain how the encoder's mental state influences actions, especially when actions are frequent, or are there anomalies in the sequence?

### Soundness
3

### Presentation
2

### Contribution
2
