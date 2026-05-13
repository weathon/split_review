# LICORICE: Label-Efficient Concept-Based Interpretable Reinforcement Learning

- Decision: Accept
- Scores: 6, 8, 6, 6, 6

## Abstract
Recent advances in reinforcement learning (RL) have predominantly leveraged neural network-based policies for decision-making, yet these models often lack interpretability, posing challenges for stakeholder comprehension and trust. Concept bottleneck models offer an interpretable alternative by integrating human-understandable concepts into neural networks. However, a significant limitation in prior work is the assumption that annotations for these concepts are readily available during training, necessitating continuous real-time concept annotation. This reliance either places a significant burden on human annotators or incurs substantial costs in API queries and inference time when employing automated labeling methods, such as vision-language models (VLMs). To overcome this limitation, we introduce a novel training scheme that enables RL algorithms to efficiently learn a concept-based policy by only querying annotators to label a small set of data. Our algorithm, LICORICE, involves three main contributions: interleaving concept learning and RL training, using a concept ensembles to actively select informative data points for labeling, and decorrelating the concept data with a simple strategy. We show how LICORICE reduces human labeling efforts to 500 or fewer concept labels in three environments and 5000 in another complex environment at minimal or no cost to performance. We also explore the use of VLMs as automated concept annotators, finding them effective in some cases but challenging in others. This work significantly reduces the annotation burden for interpretable RL, making it more practical for real-world applications where transparency is crucial.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces LICORICE, a training paradigm for efficient concept-based reinforcement learning. It reduces the need for extensive annotations. LICORICE uses active learning to label only informative data and applies data decorrelation for diverse samples. Experiment results show that LICORICE maintains performance while reducing annotation requirements.

### Strengths
1. The paper is generally well-written and structured, followed by the motivation and explanation.
2. By combining iterative training, data decorrelation, and disagreement-based active learning, LICORICE significantly reduces annotation requirements without sacrificing performance.
3. The model achieves better results compared to baseline methods.

### Weaknesses
1. During concept learning, $g$ is trained using $D_{train}$. However, as the agent's behavior changes, it may encounter new concepts during behavior learning. This can lead to a distribution mismatch between the data used for concept learning and the actual states visited during behavior learning. Specifically, the initial training data might not cover the full range of states the agent will experience as it learns, potentially causing the concept model to be inaccurate in novel situations. This could lead to suboptimal policy learning, as the agent's understanding of the environment is based on an incomplete concept model.
2. The authors mention that LICORICE reduces the need for extensive annotations. I agree with this point. However, I think right now people care more about the computation efficiency instead of the cost of labeling data. It would be better to show the training efficiency with less budget. The paper should include a detailed analysis of the computational resources required for training, including GPU memory usage and training time, and compare these metrics with baseline methods. This would provide a more comprehensive evaluation of the method's practical applicability.
3. In the budget reduction session, the authors initially use a large budget and then reduce it to a smaller one. I suggest starting with a small budget and gradually increasing it to identify the minimum human labeling effort required to maintain an acceptable reward. This approach would more effectively demonstrate the label efficiency of the proposed method, by showing how performance scales with increasing annotation effort from a minimal starting point.

### Questions
1. In Algorithm 1, please clarify the definitions of $s$ and $c$.
2. In line 187, there is an extra “the.”

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This papers proposes an active learning scheme to minimize the required concept labels for training concept policy models, which are RL policy models with concept bottlenecks. The method is simple and requires training an ensemble of concept models to estimate the disagreement for prioritizing samples for labeling. Extensive experiments show the label-efficiency of their proposed scheme over the non-active learning golden CPM, and other simple label-restricted baselines. The authors also explored replacing the concept labeling process with a VLM (gpt-4o) and find mixed results with its success.

### Strengths
## Originality

All the subcomponents of the proposed method are well-established techniques from their respective fields but chaining them together is an original contribution. The problem of label-efficiency has not been studied for CPM as well (even under-explored in general CBMs).

## Quality

The paper is extremely well written. Common questions one might have are all answered and extensively studied. This includes basic ablation studies of each component of the technique, to all the possible things one might do to a model with concept bottlenecks (e.g. intervention, automate concept labeling). The detailed documentation of experiment design (particularly the specification of how the validation set is curated in the algorithm) reflects the rigor of the work. Well done.

## Clarity

The problem statement is well formulated. The motivation is somewhat justified (though I do highly doubt whether label efficiency is the main problem for adopting CPM in place of regular policy networks in RL settings. I digress). The algorithm is well documented. Assumptions and settings are clearly stated.

## Significance

The weakest part of this paper might be its significance. It is true that interpretability via a concept bottleneck would benefit human-understanding of the decision making of RL agents. However, it does not seem like data scarcity is the biggest issue for implementing CPMs, as current settings with concepts defined all come with sufficient concept labels. If there actually exists a real life scenario where the concept labels are hard to obtain, perhaps the active learning setting makes more sense. That being said, the significant performance improvement of LICORICE over the random baseline is non-negligible.

### Weaknesses
Please refer to the questions section.

### Questions
Here are a couple of clarification questions
* In P4L120, Line18 of the algorithm states "Continue training the concept network g on Dtrain, using Dval for early stopping". Does Dtrain refer to only the new data added in this iteration, or the entire dataset collected thus far?
* In P6L285, the authors state "In Disagreement-Q, the agent similarly spends its budget at the beginning of its learning process". What does the beginning of its learning process refer exactly?
* In P9L449, Figure 3 only shows the performance of LICORICE and its variants. Including the 3 naive baselines (particularly random) would help readers understand how LICORICE relatively scale with respect to budget.

### Soundness
4

### Presentation
4

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
This paper focuses on concept-based interpretable reinforcement learning. The authors note that existing concept policy model-based methods require a large amount of concept annotations. This is typically too costly in reinforcement learning problems that require extensive interaction for policy learning. To address this issue, the authors introduce active learning, selectively annotating concepts to achieve label-efficient learning.

### Strengths
1. This work studies an interesting problem, making RL policies interpretable is important in practical applications. 
2. The proposed method indeed addresses the data challenges in the RL policy learning process. This includes separating concept learning from policy learning and using data decorrelation to focus on more diverse states. These aspects make this method more than simply applying traditional (disagreement-based) active learning. 
3. The authors validated the effectiveness of the proposed method in several environments.

### Weaknesses
1. This work emphasizes interpretable reinforcement learning, but the authors seem to have directly substituted concept learning for interpretability. I understand that concept learning can, to some extent, help improve interpretability, but the authors should demonstrate more "interpretable" results beyond just performance. I noticed that Table 4 provides definitions of concepts for each task, but how do these concepts influence the actions of different policy models? For me, the relationship between concepts and actions is what truly reflects the interpretability of decisions. For example, when the door is locked and the key is to the agent's right, the agent will move to the right; when the door is open, the agent will move towards the door. The authors should provide similar analyses to demonstrate the interpretability of decisions, rather than stopping at the accuracy of concept learning. 
2. The current experiments are mainly conducted on limited concepts. Can LICORICE be validated on a larger concept space? I suggest the authors validate their approach on more complex tasks. The chosen active learning baseline is relatively simple, but considering this is a first exploration for label-efficient concept-based reinforcement learning, it is acceptable.  
3. Finally, while it may deviate from the topic of interpretable RL, one of the greatest contributions of concept learning to RL is its ability to help RL achieve compositional generalization. I suggest including a related discussion in the section where the concept model is applied to RL.   
PDSketch: Integrated domain programming, learning, and planning. NeurIPS'22  
Programmatically Grounded, Compositionally Generalizable Robotic Manipulation. ICLR'23

### Questions
Regarding the present study, how is the aspect of interpretability substantiated? It would be beneficial to provide the specific methods or analyses employed to demonstrate the interpretable nature of the proposed approach.

---- 

After the rebuttal, most of my concerns have been addressed. I have raised my score to 6.

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
3

### Summary
Current RL methods lack interpretability, which is necessary for stakeholders to comprehend and trust them. Previous work on concept bottlenecks uses a predefined vocabulary, requiring real-time concept annotation when applied to RL. The authors propose a training scheme (LICORICE) that allows RL algorithms to efficiently learn concept-based policies by querying annotators to label only a small set of data.

### Strengths
1. The paper is well-written and easy to follow
2. The framework enables interpretability on the state estimation module of the RL framework. Human could interpret the states by reading the intermediate variables.

### Weaknesses
1. This method is not general enough. Because environments like cart pole are very simple, it’s possible to use some textual “words” to describe the state. But what about in the real environment with much more states? Also, some of the states are not describable by language. The paper's reliance on a predefined, human-understandable vocabulary limits its applicability to complex, real-world scenarios where states may involve high-dimensional sensor data or abstract concepts not easily captured by language. For example, in autonomous driving, states might include subtle changes in weather conditions or complex interactions among multiple moving objects, which are difficult to describe with simple textual concepts.
2. In line 73, the paper mentions relying on human labelers is potentially biasing the model training process. But it seems the paper doesn't mention what is the potential ground truth data (without human labeling) that is less biased. The paper proposes using VLMs (obviously, VLMs are also trained on vision-text data with human knowledge) to automate the concept extraction, but it's unclear that it will not bias the RL model training process as human labelers do?
3. line 76-90, the authors mention two concerns: 1) concept distribution learned from a policy, 2) data diversity.  But in line 91-96, the paper only mentions that the experiments are focused on human annotation and VLM-based annotation. It seems there is not a clear section to address these concerns. Ablation study shows the components are all positive. But it seems no experiment is explicitly talking about training data diversity , e.g., after applying the data decorrelation strategy how does the diversity change?
4. In line 98-99, authors claim they are the first to investigate “limited concept annotation budget for interpretable machine learning”. But there are some papers like "LABEL-FREE CONCEPT BOTTLENECK MODELS" from ICLR2023 propose CBM even without labeled concept data.
5. In those controlled environment (e.g., cartpole), I believe there might be better ways to collect state data (e.g., velocity) rather than query VLM with prompts (Appendix A.3). First, VLMs are not designed to do accurate estimation like pixel loations. Second, using simple heuristics like pattern matching the pixel of the agent may be more efficient and accurate.

### Questions
1. The original concept bottleneck models use images as input, which is already easy for human to understand. Also concept bottleneck models are intended to make the final prediction interpretable by decomposing a complex concept (e.g., an object) into its atomic-level properties, then doing classifications on top of them. But the authors mention “”opaque raw inputs”” in line 46-47. Could the authors explain more about this type of input?

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
This paper proposes a method of learning a concept-based RL policy that utilizes only a small number of annotations. Prior work introduced the concept-based RL learning for the purpose of obtaining interpretable policies, however, the assumption is that all states are annotated with the concepts. This paper proposes to sample the states and select the most informative of them with a disagreement based active learning strategy. As a result, the proposed method achieves very similar performance with much less annotated data both in terms of policy performance and concept prediction as the original method. Moreover, authors study if VLMs can be used as concept annotators in some environments.

### Strengths
- The paper addresses an important problem of making RL policies interpretable for the final users
- The proposed method removes the unrealistic assumption that all the states are annotated with the concepts. The method combines two lines of work: concept-based reinforcement learning with active learning in a novel way
- The paper studies the performance both in the case of using good quality labels and noisy labels (in the experiments it corresponds to using the environment state or VLM).

### Weaknesses
I think what I am missing the most in this paper is more explanations on the interpretability of the policy. Given that the novelty of the method is limited in a way that it combines two existing methods, it would be good to demonstrate the importance of the proposed solution more. As the goal is to produce interpretable policies, it would be good to see some examples of interpretable policies, and maybe even verify that users of the policies find them convincing and useful. Also, the paper talks about the "concepts" in a very abstract way and I would like to see some more examples of the concepts to make it more concrete. For example, table 1 shows the number of concepts and their type, but does not communicate that each concept can take more than 100 values in some cases.

Additionally, while the experimental studies are good, I think it could be further improved with some real world experiments (as the original concept-based RL paper presented the experiments in the real world) to increase the impact of the paper.

Minor questions and comments:
- How do you manage to obtain the diverse predictions in the ensemble given that they are trained in the same way?
- More details on the architecture of the policy and concept predictor would be useful
- Data decorrelation seems to be just random subsampling of the data. Is this so or is there any other important aspect? If it is the case, I don't think the authors need to discuss it in so many details.
- Does each state action pair correspond to only one concept? If there are several, how do you decide based on the disagreement in which concept to select the sample to label?

### Questions
I would like to understand a bit more about the interpretability of the policies produced by the proposed method.

### Soundness
3

### Presentation
4

### Contribution
3
