# Injecting a Structural Inductive Bias into a Seq2Seq Model by Simulation

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Strong inductive biases enable learning from little data and help generalization outside of the training distribution.
Popular neural architectures such as Transformers lack strong structural inductive biases for seq2seq NLP tasks on their own. Consequently, they struggle with systematic generalization beyond the training distribution, \eg with extrapolating to longer inputs, even when pre-trained on large amounts of text.
We show how a structural inductive bias can be efficiently injected into a seq2seq model by pre-training it to simulate structural transformations on synthetic data.
Specifically, we inject an inductive bias towards Finite State Transducers (FSTs) into a Transformer by pre-training it to simulate FSTs given their descriptions.
Our experiments show that our method imparts the desired inductive bias, resulting in improved systematic generalization and better few-shot learning for FST-like tasks. 
Our analysis shows that fine-tuned models accurately capture the state dynamics of the unseen underlying FSTs, suggesting that the simulation process is internalized by the fine-tuned model

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper creates an approach (SIP) to effectively combine FST’s topology information into transformer, through pre-training on vast amount of sampled FSTs and fine-tuned on a tunable embeddings. The author demonstrated various experimental results to support their claim that SIP is able to inject the inductive bias from FSTs into downstream tasks to achieve better performances.

### Strengths
Overall, I think the approach of injecting inductive bias that is end2end trainable is interesting, though limiting the capacity of FST by only allowing deterministic designs. The approach treats FST as a prompt prefix / soft-prompt, which is shown to help generation on “FST-like” tasks and allow the incorporate of FSTs within a larger transformer-based neural model.

1.Inductive bias from FST topology as soft-prompt for transformer supports end2end training 

2.The idea of simulation prior for generalization is interesting and the author proposes an interesting pipeline (FST data synthesis for pre-training then use average encoding for downstream task). Though I wonder what exactly is learned from the use of turnable encoding for downstream task.

### Weaknesses
I don’t think it’s very surprising that transformer is able to learn complex structure encoded from FST, especially when the pre-training data is synthetically generated with a small amount of states. 
Moreover,  the use of the current proposed framework would be limited when #states/transition explodes, in addition to that fact that positional embedding from transformer is used as normal, which made encoding of identical FSTs with different state ordering represent different things. The need to encode FST as a sequence of prefix encoding also makes the design of FST topology limited. Overall, I feel this work might scarifies too much symbolic information obtainable from FSTs in order to fit it into the prefix encoding framework. 

1.Limitation of FST which has to be deterministic.

2.The setup looks up state and transition from the embedding table which is not scalable.

3.Positional information of transformer is used as usual, which means two identical FST with different state ordering have different representation in the transformer. This could result in unwanted behavior.

### Questions
1.What exactly is learned from the tunable embedding? As the author assumes no FST information is available from downstream task, such embedding should be tuned toward certain encoding from pre-training stage right? Have the authors performed any analysis on such embedding?

2.The nature of FST accepts compositional design (that is, addition or composition of different FSTs can be easily combined). I wonder if the proposed approach, when trained on different FSTs encoding, would generalize well to the task that is solvable by their composition?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors inject an inductive bias towards Finite State Transducers (FSTs) into a Transformer by pre-training it to simulate FSTs given their descriptions. The proposed method is simple, adjustable and efficient to inject a structural inductive bias for FST-like
tasks into a Transformer. Experimental resuts show that the proposed method has better systematic generalization on tasks beyond the pre-training distribution and strong results when transferring to natural FST-like data, as demonstrated on low-resource grapheme-to-morpheme conversion.

### Strengths
1. The proposed method, which involves injecting Finite State Transducers (FSTs) into a Transformer, is novel and presents a promising direction for solving complex tasks in the real world.

2. This paper is well-written and the method is clearly described.

3. Experimental results show that the proposed method can outperform previous work in a wide range of tasks.

### Weaknesses
1. The author needs to provide more ablation experiments and analysis to understand the changes brought about by the FST on the results and why it can bring consistent improvements. Specifically, it is unclear how the learned representations within the Transformer align with the states and transitions of the FST. A more detailed analysis of the internal representations, perhaps visualizing the attention patterns or the embedding space, would be beneficial to understand the mechanism of improvement. Furthermore, the impact of different FST architectures on the final performance should be investigated, such as varying the number of states or the complexity of the transitions.

2. Despite the many experiments conducted in this paper, I still hope that the authors can apply the method to large language models. It is very important to determine whether the proposed method is still effective in LLMs and whether it can solve some problems existing in larger models, such as hallucinations. The current experiments are limited to relatively small-scale tasks, and the generalization to larger models is not guaranteed. It is important to understand how the inductive bias introduced by the FST pre-training interacts with the pre-existing knowledge and biases of large language models. The potential for the FST to mitigate issues like factual inaccuracies or logical inconsistencies in LLMs needs to be explored.

### Questions
n/a

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper explores the direction of injecting inductive biases (into Transformers) by modifying the data (particularly, through synthetic pre-training). The paper tries to inject Finite State Transducer (FST)-like biases by generating relevant synthetic pre-training data. The paper pre-trains a Transformer on the synthetic data and test it for OOD generalization during fine-tuning different FST tasks. The paper found better OOD generalization with FST pre-training and prefixes than other baselines. The paper also shows positive transfer on some natural language tasks.

### Strengths
1. Decent focused exploration on injection of inductive bias through synthetic pre-training. 

2. Shows the ability to demonstrate OOD generalizations (iteration generalization and systematic generalization) in FST-tasks from synthetic pre-training.

3. Shows transfer from pre-training on FST to some specific natural language tasks.

### Weaknesses
1. If By-T5 is already pre-trained in natural data before the synthetic pre-training, I wonder how much of an influence there is from the "pre-pre-training" in enabling OOD generalization and such. It's unclear if the observed OOD generalization is primarily due to the synthetic FST pre-training or if it's a result of the pre-existing knowledge encoded in the By-T5 model.

2. The scope feels limited. We already have prior works showing the viability of synthetic pre-training and knowledge transfer from natural language tasks. It is not as clear what the motivation for exploring particularly FST-related tasks is. Transformers have been shown to underperform in OOD generalization on logical inference [1,2], ListOps [2], Flip-Flop languages [3], parity tasks/sensitive tasks [4], automata tasks [5], and others [6]. It would have been good to contrast the approach with some of such works, reconcile with them, and see if the synthetic pre-training proposed here can be used. The paper does not adequately address how the proposed method compares to these known limitations of Transformers in tasks requiring systematic generalization.

### Questions
1. What are the average and maximum sequence lengths in the pre-training data, training data, and iteration generalization data? 

2. Would it be possible to explore generalizations to higher lengths e.g. 100 or more?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
