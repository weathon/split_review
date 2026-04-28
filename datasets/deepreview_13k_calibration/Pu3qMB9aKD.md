# Form follows Function: Text-to-Text Conditional Graph Generation based on Functional Requirements

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5

## Abstract
This work focuses on the novel problem setting of generating graphs conditioned on a description of the graph's functional requirements in a downstream task. We pose the problem as a text-to-text generation problem and focus on the approach of fine-tuning a pretrained large language model (LLM) to generate graphs. We propose an inductive bias which incorporates information about the structure of the graph into the LLM's generation process by incorporating message passing layers into an LLM's architecture. To evaluate our proposed method, we design a novel set of experiments using publicly available and widely studied molecule and knowledge graph data sets. Results suggest our proposed approach generates graphs which more closely meet the requested functional requirements, outperforming baselines developed on similar tasks by a statistically significant margin.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces the problem of generating graphs conditioned on its functional requirements as a text-to-text generation task. Experiments were conducted on a novel formulation of PCQM4M for text graph generation, as well as WebNLG+ 2020. The proposed approach involves graph serialization / de-serialization that handles node disambiguation, a variant of the negative log-likelihood objective, and interleaving message passing layers between transformer layers to pass information via a graph's edge graph (or variants) with causal graph attention masking.

### Strengths
The paper is written clearly and is mostly easy to follow. The diagrams in the paper are very well done and illustrate the described methods appropriately. Figure 1 in particular was extremely helpful in understanding the approach.

The problem of text-to-graph generation based on functional requirements is a problem area that is underexplored, and this paper is a good contribution to it. In particular, the reformulation of PCQM4M is a helpful new resource for this task that this paper provides.

### Weaknesses
- The paper does not explain the reasoning for formulating the training objective as it is in Eqn 1. This is surprising given that experiments in Appendix D show a difference when using the differing term, but no satisfactory reason was given for why this might be the case. The lack of explanation makes it difficult to understand the motivation behind the specific form of the objective function and why it deviates from the standard autoregressive objective in Eqn 2. This is a critical point, as the training objective is a core component of the proposed method, and the absence of a clear rationale undermines the validity of the approach.

- The experimental results are not very convincing of the importance of the message passing layer, as the SGG-LLM experiments with message passing enabled are not statistically significantly better than with message passing disabled (with reference to Table 2). Specifically, the reported MAE on the QED dataset shows an improvement of 0.008, which is within the margin of error (0.036 +/- 0.005 vs 0.044 +/- 0.011), suggesting that the message passing component may not be contributing substantially to the overall performance. This raises concerns about the necessity and effectiveness of the added complexity introduced by the message passing layers.

- The feature vector for a node vector was selected as the feature vector of the last element describing that node. The paper does not provide any justification for this choice, nor does it explore other potential aggregation methods, such as mean-pooling or max-pooling. This lack of experimentation and justification raises questions about the optimality of the chosen approach and whether alternative aggregation strategies could yield better results.

### Questions
**Questions**:

1. Baseline without fine-tuning: Under Appendix D, how was the SSG-LLM w/out fine-tuning prompted? Was there any investigation done using in-context learning / few-shot prompting to get a parsable generation?

2. As per Figure 1, is the reason that graph masking includes a self node (node i attends to node i) the same reason that causal masking has a token attending to itself? Is there any specific reason not to exclude that self node?

3. What is the reasoning for the formulation of the denominator in Eqn 1, and why must it differ from Eqn 2 for training on serialized graph sequences? Seems there is a missing explanation in the paragraph right under Eqn 2.

4. The feature vector for a node vector was selected as the feature vector of the last element describing that node. Were there any experiments done to vary this, for e.g. mean-pooling?

5. Why was BLOOM selected as the LLM backbone?

6. With reference to Table 3, why was parsability affected when using message passing?

7. With reference to Table 2, it seems that much of the improvement of SGG-LLM was in fine-tuning on the QED/Valency dataset. Moreover, the MAE on the QED dataset shows that the performance improvement when enabling message passing is not statistically significant (0.036 +/- 0.005, vs 0.044 +/- 0.011). Can the authors please highlight arguments for why the message passing inductive bias is working correctly, and what might be the issue in the current approach?


**Suggestions**:
- In Section 1, the paragraph on causal masking seems out of place. Suggest moving it to Section 3.1 before introducing causal graph masking.
- It is difficult to distinguish between the colours used in Tables 2 and 3. Would suggest finding a more accessibility-friendly solution, like using icons to distinguish between rows.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new problem of graph generation based on given graph properties. The authors propose to use LLMs for graph generation. They add graph message passing layers into LLMs for capturing graph features based on graph structure.

### Strengths
* This paper proposes some techniques to solve the ambiguous nodes and incorporate graph structures when using LLMs for graph generation.

### Weaknesses
 * The task appears to be ill-defined. The authors claim to introduce a "novel problem setting," but fail to provide a clear problem definition. It remains unclear what the key challenges of the proposed property-to-graph generation task are. Additionally, the evaluation dataset and metrics lack soundness discussion. If the evaluation benchmark can be derived from previous works with little modification, why not using the same benchmark and metrics in previous works? The authors should thoroughly address the suitability of the datasets and metrics. Baselines are also inadequately explored, and the results are far from convincing.
* The technical contribution is also limited. The primary contribution emphasized by the authors involves the use of causal masks during generation. However, the employment of causal masks for autoregressive generation is just a trick to ensure efficient training. (Otherwise, it will require to train on each token independently with multiple passes.) It's weird to label this well-known technical detail as the key contribution.
* The paper is hard to follow.

### Questions
* See weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies text-to-graph generation with large language models. The authors propose a new fine-tuning method in which LM fine-tuning and message-passing (MP) are interleaved. Empirical results indicate the effectiveness of the approach. 

The problem in question is interesting, but I have some concerns:

(1) the technical contribution is not clear to me.  It seems that interleaving with MP is the only technical contribution, however, when the number of fine-tuning examples increases, the model without MP can achieve much better performance (half MAE on QED), then what will happen if we fine-tune the model on 400k examples with MP? is it possible that w/ MP and w/o MP are comparable when there are enough fine-tuning examples? Moreover, why the results on QED and Valency are inconsistent on 400k examples? 

(2) the presentation needs improvement. I find conflict in some descriptions. For example, in the third line from the bottom in Page 4, it is said that "regen only differs from our proposed model SGG-LLM without message passing in that it was trained using equation 2 instead of 1" but in the third line from the top in Page 16, it is said that "regen is a model trained with equuation 1". I am confused with such presentations. Then what is the true difference between the proposed method and the baseline? It is also important to highlight the major contributions in Introduction.

### Strengths
interesting problem

### Weaknesses
The paper studies text-to-graph generation with large language models. The authors propose a new fine-tuning method in which LM fine-tuning and message-passing (MP) are interleaved. Empirical results indicate the effectiveness of the approach.

The problem in question is interesting, but I have some concerns:

(1) the technical contribution is not clear to me.  It seems that interleaving with MP is the only technical contribution, however, when the number of fine-tuning examples increases, the model without MP can achieve much better performance (half MAE on QED), then what will happen if we fine-tune the model on 400k examples with MP? is it possible that w/ MP and w/o MP are comparable when there are enough fine-tuning examples? Moreover, why the results on QED and Valency are inconsistent on 400k examples?

(2) the presentation needs improvement. I find conflict in some descriptions. For example, in the third line from the bottom in Page 4, it is said that "regen only differs from our proposed model SGG-LLM without message passing in that it was trained using equation 2 instead of 1" but in the third line from the top in Page 16, it is said that "regen is a model trained with equuation 1". I am confused with such presentations. Then what is the true difference between the proposed method and the baseline? It is also important to highlight the major contributions in Introduction.


### Questions
see the summary

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new graph generation framework based on pretrained LLM. The paper formulates the graph generation problem as the generation of a serialized graph. The paper first proposes a serialization method that reversibly serializes any graph by converting the node graph into an edge graph. The paper also slightly changes the weight of NLL loss to ensure each instance is weighted equally. The paper finally proposes a new message-passing layer above the language model. The paper conducts experiments on molecular and WdbNLG graph generation and achieves competitive results.

### Strengths
1. The paper proposes a new graph generation technique based on pretrained LLMs. The paper first modifies the weight of the NLL loss. The paper then inserts a message-passing layer into the standard transformers. The paper finally proposes a new edge graph to reduce node ambiguity. 
2. The paper conducts experiments on molecular generation for QED and valency. The proposed framework achieves significant improvements compared to other baselines. The paper further analyzes its parsability and diversity. Additionally, the paper also conducts experiments on the WebNLG tasks to show its generalization ability. The paper includes an additional ablation study in the Appendix. 
3. The paper provides code. The paper provides comprehensive implementation details in the Appendix.

### Weaknesses
1. The idea of message passing for molecular graphs is incremental. For example, Klicpera et al., show message passing is important for molecular graphs, although their message-passing function is different from this paper. The idea of fine-tuning objectives is also an engineering trick rather than a model contribution. 
2. BLOOM is not a suitable baseline for molecular generation since it is not trained on molecular data. Galactica (Taylor et al., 2022) would be better since its training data includes smile strings. The simple autoregressive model can outperform the proposed message passing by increasing its training set. 
3. The language in the paper needs to be further polished.

### Questions
Is it possible to include additional analysis for Table 3, since sometimes baselines perform better?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
