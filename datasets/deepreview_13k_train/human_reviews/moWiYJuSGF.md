# Web Agents with World Models: Learning and Leveraging Environment Dynamics in Web Navigation

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Large language models (LLMs) have recently gained much attention in building autonomous agents. However, performance of current LLM-based web agents in long-horizon tasks is far from optimal, often yielding errors such as repeatedly buying a non-refundable flight ticket. By contrast, humans can avoid such an irreversible mistake, as we have an \textit{awareness} of the potential outcomes (\eg losing money) of our actions, also known as the ``\textit{world model}''.
Motivated by this, our study first starts with preliminary analyses, confirming the absence of world models in current LLMs (\eg GPT-4o, Claude-3.5-Sonnet, etc.). Then, we present a World-model-augmented (WMA) web agent, which simulates the outcomes of its actions for better decision-making.
To overcome the challenges in training LLMs as world models predicting next observations, such as repeated elements across observations and long HTML inputs, 
we propose a transition-focused observation abstraction, where the prediction objectives are free-form natural language descriptions exclusively highlighting important state differences between time steps. Experiments on WebArena and Mind2Web show that our world models improve agents' policy selection without training and demonstrate superior cost- and time-efficiency compared to recent tree-search-based agents.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes an approach for enhancing the performance of LLM-based web agents in long-horizon tasks. The authors introduce a World-Model-Augmented (WMA) web agent that simulates the outcomes of its actions through a "world model." This design enables the agent to anticipate the effects of actions, thus reducing errors and improving decision-making in dynamic web environments. By employing a transition-focused observation abstraction, the model processes large state transitions without redundant data. Experiments conducted on WebArena and Mind2Web indicate that the WMA agent outperforms other agents in various metrics.

### Strengths
1. The paper considers the application of world models within LLM-based web agents, creating an interesting direction for improving policy selection in web-based navigation tasks.

2. The proposed transition-focused observation abstraction helps to reduce redundant data, lowering computational costs and allowing the model to focus on critical changes.

3. The authors show that the WMA model can be easily integrated into existing web agents, making it a versatile addition to LLM-based navigation models.

### Weaknesses
1. While the paper demonstrates improved single-step action selection, it does not address multi-step planning comprehensively, which is crucial for certain long-horizon tasks. The evaluation focuses on immediate action prediction, but the true value of a world model lies in its ability to facilitate long-term reasoning and planning. The paper lacks experiments that demonstrate the model's capacity to plan over multiple steps, which is essential for complex web navigation scenarios where a sequence of actions is required to achieve a goal.

2. The approach is limited to text-based web interactions, and although HTML trees are effective, omitting visual elements could restrict the model's applicability in web navigation tasks where visual cues are essential. Many web interfaces rely heavily on visual elements such as icons, images, and layout for user interaction. By focusing solely on text and HTML structure, the model may struggle to navigate web pages where visual information is critical for identifying interactive elements or understanding the context of the page. This limitation could significantly reduce the model's effectiveness in real-world web environments.

3. While the transition-focused abstraction reduces redundancy, it may oversimplify complex web elements, potentially leading to reduced accuracy in actions involving nuanced page layouts. The abstraction process, by focusing on differences between states, might discard subtle but crucial details present in the full HTML structure. For example, changes in CSS classes or minor alterations in the position of elements, which might be important for certain actions, could be overlooked. This simplification could lead to the model making incorrect assumptions about the state of the page, especially in complex layouts.

4. The paper does not discuss how the proposed world model scales when dealing with significantly larger action spaces, which is critical for broader applicability. In real-world web navigation, the number of possible actions can be very large, especially when considering all clickable elements, form inputs, and other interactive components. The paper does not provide any analysis or experiments on how the model's performance and computational efficiency are affected by an increase in the size of the action space. This lack of scalability analysis raises concerns about the model's practicality in more complex web environments.

### Questions
1. Can the model extend to handle visual inputs alongside text-based observations? This would make it more versatile for environments where visual information is vital.

2. How does the model perform in extended multi-step planning scenarios? Would recursive application of the world model effectively address multi-step planning challenges?

3. How does the observation abstraction perform in very dynamic web environments? In fast-changing states, does it retain relevant information, or does it risk omitting crucial details?

4. What is the impact of scaling the action space on the computational efficiency of the WMA model? Would the model maintain its efficiency with a larger action candidate set?

### Soundness
2

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
This paper explores using explicit world models in LLM-based web agents. An (explicit) world model is a model able to predict the future state given an action on the current state. Their preliminary analysis shows that existing models cannot successfully predict the results of their actions, but that knowing that information would significantly help LLM-based agents. 

Their contributions are 
1) a training algorithm for web-agent world models that predicts an abstracted version of the transition to the observation after an action is applied. 
2) an algorithm for using the world model to improve performance. 

The training algorithm uses trajectory data to produce observation diffs from each action, then summarizes these changes with an LLM. The world model LLM is then trained to output the summaries (predict what will change in natural language)

The policy optimization algorithm uses a trained value function in addition to the world model. It works by sampling multiple potential actions, using the world model to predict changes, and then using the value function to predict the value. This can be thought of as a two-step Q-value function where the first step is the world model and the second step is evaluation. The value function is trained using reward data from Mind2Web. 

They have main results on WebArena and Mind2Web. There is also further analysis by category, and other experiments, including ablations over the reward estimation, training of world model, and use of abstracted observations.

### Strengths
Originality:
The paper provides an original algorithm for training web-agent world models and an original algorithm for using such models to improve LLM-based web agents. 

Clarity:
The clarity of the problem domain is quite good. The introduction lays a good case for how world models could improve web agents. The approach is quite clear. Figure 3 is nice. There is some breakdown of the clarity for some of the results but overall it was easy to follow along and understand what was being done. 

Significance:
The utility of world models for web-agents is quite clear but still under-explored. Both the training and inference time algorithm presented here could have significance down the line.

### Weaknesses
The primary weakness of this paper is that the main results are quite weak. On WebArena, this significantly underperforms the listed baselines, and other newer baselines also exist.

The second weakness is that it is not always clear what is being tested or shown. There are a number of questions (see below) that need to be clarified. Specifically, the relationship between the value function and the world model is unclear. The value function is trained to output both a score and text, but the training objective is not clearly defined, and it's unclear how this interacts with the abstracted observations from the world model. Furthermore, the Q-value function is also fine-tuned, but it's not clear if it uses the same training procedure or if it is given the ability to reason about the action's effects before outputting a value. This makes the ablation study in Table 5 potentially unfair.

To me the paper should focus more on the web-agent *world model* than on the web agent itself. There is some analysis on failure modes but not enough analysis on the world model itself. This may stem from the fact that abstract transition representations may be hard to analyze. A full world model would be able to show things like per-element accuracy. Perhaps there are other creative ways to analyze how to assess the learned world model and how it functions.

The paper really dives into this one way of using the world model when it could take a broader view. For instance, why not use WMA/policy optimization

### Questions
Clarifying questions:

1) What is “policy optimization” as applied to Tree Search Agent (Kuh et al, 2024). I thought Figure 3 bottom shows “policy optimization” which seems like it would only apply to World Model Agent. 

2) Correspondingly, what is "no policy optimization"? Is that just CoT? If so, why are the results different? Why is Tree Search Agent better?

3) Is value function trained with the world model data or is it a pure value function? If pure value function, how does that work with the abstracted observations? 

4) Line 284: I don’t get this line and how the citation matches. “explore diverse next states st+1 ∈ S (Wang et al., 2022)”

5) Table 5: The value function is fine-tuned. Is the Q-value function being fine-tuned as well and in the same way? If not, does not seem like a fair ablation. Also, is the Q-value function given ability to reason about what the action will do before outputting the value?
Other questions:

6) Why is the user instruction included in the data? Shouldn't the world model be able to predict the changes based on the action without needing to know the intent?

7) Table 2: Why not include the baselines from table 1? At least the tree search agent which is repeatedly compared to. 

8) Figure 1 shows that commercial LLMs cannot predict the next state well by looking at actual observations. Perhaps they would be able to pick the correct abstracted transition-focused observation? Running that same experiment with the transition focused observation version (ground truth, not predicted) could be interesting. 

9) Which leads me to the following question, how do larger commercial LLMs fare at predicting the next abstract transition? It would be nice to see Table 5 row 2 with a few different base LLMs. 

10) Why is HTML-T5 considered SOTA for Mind2Web? It seems like there are many much stronger algorithms presented in table 1. Mind2Web is also an offline evaluation dataset so does not account for different ways of completing a task or different action spaces. 

Other notes:

11) Line 184: “These findings highlight the necessity of world models in LLM-based web agents”: 
- Not sure I agree with this. I would say something more like, “This findings highlight the benefit world models could provide to LLM-based web agents”.
- The findings show that (my words) “LLMs do not have good world models for web activity” and “having a better world model would improve web agent performance”. This does not add up to “necessity”

12) “In Table 1 (middle), we first compare our WMA web agent (16.6%) with vanilla CoT (13.1%) and observe significant improvements over almost all domains in WebArena as detailed in Table 2.” 
This is confusingly written. Table 1 is the main table and there is only half a sentence of analysis. 

13) I do not like the y-axis bounds selection on many of the figures. It would be easier to read with 0 as lower bound (or at least a bit more space). E.g. Figure 6 is hard to tell what the k=1 line is at.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposes Wold-Model-Augmented (WMA) web agents. The authors present detailed analysis on the inability of current LLMs in estimating action consequences on the web and propose to abstract webpage state presentation as state transition description in natural language accordingly. Based on the abstraction, a world model for web navigation is trained and used for enhancing web agents. On two popular benchmarks, WebArena and Mind2Web, the proposed WMA web agent shows sizable performance gain over the baseline LLM and demands lower cost than tree-search methods.

### Strengths
1. To the best of my knowledge, this work is among the first to employ the world model in web agents. Its technical contribution includes a novel state representation, world model training method, and world model augmented agent design.
2. The resulting method shows improved performance and higher efficiency over baselines.
3. The experiment setup is overall reasonable. The authors provide sufficient ablation study and detailed analysis on performance, efficiency, and error distribution, contributing valuable insights to the community.
4. The writing and presentation of this paper is clear and easy to follow.

### Weaknesses
1. The experiments only cover end-to-end evaluation of agent performance. A directly evaluation on world modeling performance would be helpful for understanding the quality of the world model itself. For example, this evaluation can follow the same setting as the analysis of section 3. Specifically, a metric that quantifies the overlap between predicted and actual state transitions would be valuable. This could involve measuring the precision and recall of predicted state changes against the ground truth, focusing on the accuracy of the abstracted state representation and the fidelity of the predicted transitions.
2. The performance of Vanilla CoT and WMA web agent w/o policy optimization differs (13.1% vs 12.8% in Table 1). What are the differences between them? In addition, WMA web agent underperforms the tree search agent. Although tree search leverages additional signals and more compute, I think it is important to discuss if WMA web agent could scale to higher compute and deliver competitive performance under similar budget. It would be beneficial to explore the computational scaling properties of the WMA agent, investigating how performance changes with increased training data or model size, and whether it can approach the performance of tree search methods with comparable computational resources. A detailed analysis of the computational cost of both methods would also be valuable.
3. The proposed method and evaluation is limited to the text modality. Recent studies have suggested that visual features are critical for good web navigation performance. It remains unclear if WMA could adapt to multimodal settings and advance the state-of-the-art of web navigation. The current method relies solely on the text-based representation of the webpage (HTML and accessibility tree). The lack of visual input may limit its ability to handle complex web layouts and dynamic content. It is important to investigate how the WMA framework can be extended to incorporate visual information, such as screenshots or rendered page views, and whether this would lead to improved performance.

### Questions
1. In section 4.1.1, training data for the world model is sampled from an LLM as web agent. Does this strategy create a dependency between the world model and the underlying agent, which could potentially hinder generalization?
2. The proposed method, particularly the state abstraction method, is limited to the text modality (HTML and accessibility tree). Can it be easily extended into a multimodal setup?
3. As stated in weaknesses, clarification of Vanilla CoT and WMA web agent /o policy optimization is needed.

### Soundness
2

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
4

### Summary
This paper explores the introduction of world knowledge models into the field of agents, particularly within the context of web navigation. Specifically, the study finds through exploratory experiments that 
1. existing large models lack sufficient predictive capability regarding the consequences of their actions. 
2. Enabling these models to anticipate such consequences can significantly enhance their planning capabilities. 
Based on this finding, the authors trained a world knowledge model (WKM) to predict the potential outcomes of an action.  The proposed transition-focused observation abstraction plays a crucial role in the training stage.
The paper conducts comprehensive experiments to demonstrate the necessity and superiority of using WKM.

### Strengths
1. The introduction of this paper is well-constructed. Through experiments, it identifies the issue that existing models cannot effectively predict the potential consequences of their actions, and it highlights that enabling models to understand these consequences can enhance their planning capabilities. The proposed approach is very reasonable.
2. The explanations in this paper are clear and easy to understand. The formulas and figures effectively illustrate the method proposed by the authors.
3. The authors conducted multi-dimensional experiments that effectively address potential questions from readers.

### Weaknesses
1. Although this paper claims to be the first to introduce a world knowledge model into LLM-based agents, to my knowledge, this may not be the case. For example, the work "Agent Planning with World Knowledge Model" might also explore this area. The authors may need to conduct a more extensive literature review to compare and discuss the similarities and differences between their proposed method and existing approaches.
2. The performance improvement brought by the experiments in this paper is not significant. Additionally, the authors' WKM is limited to a depth of 1. It might be worth considering deeper levels.

### Questions
1. As discussed in weakness 1, could the authors conduct a more extensive literature review to discuss the similarities and differences between existing WKM-based methods and their proposed approach? Although this is mentioned in section 6.1, too few works are considered.
2. As discussed in weakness 2, while the authors have considered the impact of exploration breadth in WKM during the ablation study, could they conduct experiments to consider the impact of depth as well?
If the authors can adequately address the questions above, I would be willing to reconsider the review.

### Soundness
3

### Presentation
3

### Contribution
2
