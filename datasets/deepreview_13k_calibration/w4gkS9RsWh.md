# Think or Remember? Detecting and Directing LLMs Towards Memorization or Generalization

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5

## Abstract
In this paper, we study fundamental mechanisms of memorization and generalization in Large Language Models (LLMs), drawing inspiration from the functional specialization observed in the human brain. Our study aims to (a) determine whether LLMs exhibit spatial differentiation of neurons for memorization and generalization, (b) predict these behaviors using internal representations, and (c) control them through inference-time interventions. To achieve this, we design specialized datasets to distinguish between memorization and generalization, build up classifiers to predict these behaviors from model hidden states and develop interventions to influence the model in real time. Our experiments reveal that LLMs exhibit neuron-wise differentiation for memorization and generalization, and the proposed intervention mechanism successfully steers the model's behavior as intended. These findings significantly advance the understanding of LLM behavior and demonstrate the potential for enhancing the reliability and controllability of LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper explores memorization and generalization in large language models (LLMs), inspired by the functional specialization observed in the human brain. The authors want to determine whether LLMs show differentiation among neurons when performing memorization or generalization, then use techniques to predict which behavior the model is likely to perform based on activations. And, lastly, implement inference-time interventions to direct models towards memorization or generalization as needed.

### Strengths
- The paper tackles a highly relevant problem in the field of LLMs—understanding and controlling the behaviors of memorization and generalization.
- The paper is clearly written, with a logical flow. The research questions and objectives are well-defined, making the study’s purpose and approach easy to follow.
- The authors construct specialized datasets that distinguish between memorization and generalization. This setup provides a good base for analysis

### Weaknesses
 - The hypothesis that certain neurons control specific behaviors based on brain function?  While inspired by brain functionality, the paper doesn’t fully substantiate or utilize the correlation to neuroscience. 

- The method relies on having a specialized dataset to differentiate between behaviors, which may limit practical applicability. Furthermore, the study only considers a single task; in real-world applications, models are often fine-tuned across multiple tasks, which may affect behavior control.

- Is the behavior shift strictly binary, meaning that applying a shift immediately moves the model to the other state (e.g., from memorization to generalization)? 

- The focus on neuron-level interventions may be too granular. As this requires identification of neuron behavior using custom datasets. Exploring higher-level interventions, such as prompting or input changes to toggle memorization or generalization, might be more relevant? Thoughts?

### Questions
- As selecting appropriate values for topN and alpha is crucial for achieving the desired behavior shift, how can this be optimally chosen for different archs, datasets and tasks? This can also be a drawback?
- For the intervention, is the adjustment applied to all neurons or limited to those in the final layers? Visualizing the number of neurons impacted and identifying the specific layers they belong to would provide valuable insights
- Also could you please explain what is meant by "spatial" differentiation in this context

### Soundness
3

### Presentation
3

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
This paper uses two synthetic dataset to detect whether a model engages in memorization or generalization behaviors. The analysis is done in three stages: (1) determining if neurons in LLMs differentiate spatially for memorization versus generalization, (2) predicting these behaviors based on hidden states, and (3) influencing LLMs to switch between these behaviors through real-time interventions. They find that deep layers are responsible for the two distinct behaviors and show that model behaviors can be controlled.

### Strengths
1. The paper aims to address an important question — whether the model engages in memorization or generalization. The question is of great importance for developing trustworthy AI and has broad applications, such as privacy-sensitive LLMs. 

2. The analysis goes beyond simply “passively” detecting distinct neuron activation patterns; it also includes “actively” steering the model toward specific behaviors. By combining these approaches, the authors effectively differentiate the mechanisms LLMs use when engaging in memorization versus generalization, offering a more comprehensive understanding of these behaviors.

### Weaknesses
1. The study primarily focuses on relatively small models (GPT-2 and GPT-2-medium) and small synthetic datasets. For a paper aiming to establish an empirical pattern, a more comprehensive analysis across a range of model sizes and a broader set of tasks—ideally including less synthetic, real-world tasks—would strengthen the findings and increase confidence in the generalizability of the results. The use of GPT-2 variants, while convenient, limits the applicability of the findings to more modern architectures and larger parameter scales. Furthermore, the synthetic datasets, while allowing for controlled experiments, may not capture the complexities of real-world data, thus raising questions about the ecological validity of the observed memorization and generalization behaviors. It would be crucial to demonstrate that these patterns hold in more realistic scenarios.

2. The authors designed two synthetic datasets to observe distinct behaviors in models, serving as indicators of memorization versus generalization. However, the patterns identified appear limited to these specific datasets. To effectively demonstrate (a) whether LLMs exhibit spatial differentiation of neurons for memorization and generalization, and (b) the predictability of these behaviors based on internal representations, it would be important to show that the observed spatial differentiation generalizes across tasks (pattern in task A generalize to task B). From the current experiments on two tasks with two different models, the main unifying insight seems to be that behavior differentiation occurs in the later layers, which may not fully establish the robustness of the findings across varied contexts. The lack of cross-task validation weakens the claim that the identified neuron activation patterns are robust indicators of memorization and generalization, rather than being specific to the chosen synthetic tasks. Showing that the same neurons are consistently activated for memorization or generalization across different tasks would significantly strengthen the paper's claims.

3. The method of detecting differences in hidden layer activations is relatively straightforward, and as noted in the first point, the findings may be limited in their novelty and broader applicability. It remains unclear whether the paper offers substantial new insights or practical implications at scale for advancing our understanding or control of LLM behaviors. The analysis relies on basic activation differences, which may not capture the complex interplay of neurons within the network. A more sophisticated analysis, perhaps involving methods from network analysis or information theory, could reveal more nuanced patterns. The current approach, while simple, may not be sufficient to provide deep insights into the underlying mechanisms of memorization and generalization.

### Questions
Could you clarify the experimental procedure? In particular, I am confused about:   
 
1. “The training process involved presenting each instance in its entirety to the LLM rather than as a QA pair. “ Are you finetuning with a causal language modeling objective? Could you give some concrete examples?
   
 2. “During training, we continuously monitored the model’s ability to perform memorization and generalization on a test set and preserved the model once it demonstrated both behaviors. “ Could you explain why you use this behaviors instead of (1) train until convergence (2) train until performance has reached a maximum on a validation set. The current choice seems an unnatural one compared to the usual practice.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The work investigates the research question: whether the generalization behaviours and the memorization behaviours of language models (given similar inputs) correlates to some specific regions of neuron values inside the models? With GPT-2 and two specific task settings, the authors manage to identify such regions, leverage them to predict models' behaviours (generalizing versus memorizing) and control models' behaviour through inference-time intervention methods.

### Strengths
1. the paper is well-writen and very easy to follow.
2. the key research question in the paper "whether the generalization behaviours and the memorization behaviours of language models (given similar inputs) correlates to some specific regions of neuron values inside the models?" is quite important and interesting as well.
3. the experiments conducted in the paper are multi-faceted, cross-validating the presented results of each part.

### Weaknesses
1. The experiments (regarding the two synthetic dataset settings, the language model scales) is quite limited, making the reviewer question the generality of the conclusions derived in the paper.
2. The technical contribution of the paper is also limited (e.g., in the third experiment part, ITI is mostly from Li et al., 2024). The causal analysis part is also adopted in many previous works. Though authors leverage them to investigating this new research question, this point stil weaken the overall contribution of the paper.

### Questions
1. Did you train the GPT-2/GPT-2-Medium from random initialization? Or just fine-tune the model with designed datasets?
2. Since the re-phrase the input prompts still introduce additional variables, did you try forward the same inputs multiple times and observe whether the language models behave differently (i.e., memorize or generalize)?

### Soundness
3

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
4

### Summary
This paper studies the differentiation between memorization and generalization mechanisms in LLMs. By designing specific datasets, the authors observe the neurons in LLMs show different behaviors associated with memorization and generalization, and they analyze this differentiation in view of neuron-wise mean difference. In addition, the authors build classifiers to categorize memorization behavior and generalization behavior, enabling controlled adjustments (towards memorization or generalization) to the LLM’s output during inference.

### Strengths
- This paper addresses a challenging and interesting problem in LLM research.
- The paper has a very clear research question and a well-defined study domain, enabling a focused investigation.

### Weaknesses
 - While the definition of memorization is clear in this study, the definition of generalization remains somewhat ambiguous. The author defined in the paper “generalization involves generating outputs through correct reasoning”, but how to define “correct reasoning”? For example, if a response shows partial memorization, does it still in the case of generalization? The authors distinguish between memorization and generalization only based on two simple datasets, making the scope of the study limited.

- The paper assumes a strict distinction (as they design a binary classifier) between memorization and generalization based on the LLM’s output. However, in reality,  LLMs often generate answers based on both mechanisms. In addition, the construction of the dataset may lead the model to overfit memorization patterns, which increases the bias of the model.

- The rate of the behavior change in response to the designed pairs are relatively low (11% for in-context inference and 8.5% for arithmetic tasks). Although the author mentioned that one "could continuously generate different test instances to collect the desired pairwise representations". However, dose this still support the results? or if it introduces the risk of random guessing. 

- The paper uses "neuron-wise mean difference" to show neurons behavior change according to different pairs, however, a detailed analysis is missing, such as how the values correlate with memorization or generalization mechanism. Does the behavior change specific to models and dataset or rather applicable towards general models and datasets?

- In addition to the point above, the paper only evaluate each dataset on one model, it is not sure the results and the intervention are model-specific or broadly applicable.

Minor:
- The font in Figure 3 and Figue 4 is too small to read.

### Questions
- What is model’s overall performance after training on the two datasets? Does the introduction of memorization patterns influence the model performance?

- The paper computed the NMD for each neuron, have the authors considered the influence of the cluster or interactions between neurons in the behavior change?

- What does “other” mean in Table 1 and table 2?

### Soundness
3

### Presentation
3

### Contribution
2
