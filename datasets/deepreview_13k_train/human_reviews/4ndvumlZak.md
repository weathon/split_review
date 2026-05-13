# Closing the Gap between Neural Networks for Approximate and Rigorous Logical Reasoning

- Decision: Reject
- Scores: 5, 5, 5, 3

## Abstract
Despite the historical successes of neural networks,
the rigour of logical reasoning is still beyond their reach. Taking syllogistic reasoning as a subset of logical reasoning, we show supervised neural networks cannot reach the rigour of syllogistic reasoning, mainly because they use composition tables, which are coarse to distinguish each valid type of syllogistic reasoning and because end-to-end supervised learning may change the premises. As Transformer's Key-Query-Value structure is a combination table, we conclude that neural networks built upon Transformers cannot reach the rigour of syllogistic reasoning and, thus, cannot reach the rigour of logical reasoning. We logically prove that oversmoothing, in the setting of part-whole relations, can be avoided, if neural networks use region embeddings, and propose the method of reasoning through explicit constructing and inspecting region configurations, to achieve the rigour of logical reasoning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes a task that converts syllogism into subset relations and then generates an image dataset that visualizes the subset relations and evaluates neural networks. The authors show in their experiments that although Euler Networks can learn part-whole relations between two entities, it cannot learn complex combinations of these relations, resulting in a lack of validity in the equivalent syllogism reasoning. Furthermore, the authors hypothesized that NNs should use one-hot representation to acquire the rigorous reasoning ability.

### Strengths
- The paper presents an important question that the community really cares about.
- The author shows the equivalence between syllogism reasoning and part-whole relations, and converted reasoning task into a visual prediction problem, which is interesting to me.

### Weaknesses
 - This paper still lacks enough experiments to support the authors' claims. Why would a one-hot representation save neural nets in reasoning soundness issues?
- The presentation of this paper could be further improved. The structure of it now looks more like a technical report. It lacks of figures and charts to present the experimental results.
- The discuss is high-level, while the technical detail or insufficiency of the compared methods are not discussed enough.

### Questions
Please see above.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors highlight the limitations of neural networks, including large language models (LLMs), in achieving rigorous syllogistic reasoning, which is essential for logic and human rationality. They argue that these networks should avoid combination tables and instead use non-vector embeddings to prevent oversmoothing. The paper reviews the Siamese Masked Autoencoder and presents experiments demonstrating that models relying on combination tables cannot attain 100% accuracy in syllogistic tasks. However, using non-vector embeddings as computational building blocks can help neural networks avoid oversmoothing. This work aims to bridge the gap between neural networks for approximate and rigorous logical reasoning.

### Strengths
- The authors substantiate their claims with experimental results, showcasing the shortcomings of existing models, such as the Siamese Masked Autoencoder, in achieving high accuracy in syllogistic reasoning.
- The paper opens avenues for further exploration, encouraging researchers to develop architectures that can effectively address rigorous reasoning tasks.

### Weaknesses
The authors claim three main contributions, and there are corresponding weaknesses for each:

   - **Contribution 1:** The authors conduct an experiment in Section 4. However, the experiments in Sections 4.1 and 4.2 appear to primarily test neural models' performance on out-of-distribution inputs. The poor performance of neural models on out-of-distribution inputs is already well-documented, which limits the novelty of this contribution. Specifically, the experiments seem to introduce variations in the input data (e.g., single green circles instead of two), which inherently tests the model's generalization capabilities rather than its core reasoning abilities. This is a standard challenge for neural networks and does not provide a novel insight into the limitations of syllogistic reasoning.

   - **Contribution 2:** The use of combination tables is discussed in Section 4.3, but this section is confusing. For example, the authors state that the combination table only generates the conclusion "all V are U" is not enough, since it misses the conclusion “some V are U.” However, the statement "all V are U" clearly describes a part-whole relationship, and "some V are U" can be derived from "all V are U." The authors did not explain why this senario is worse. The argument lacks a clear explanation of why the inability to directly generate “some V are U” from a combination table that produces “all V are U” is a significant limitation. It is not clear why a system that can infer “some” from “all” is considered deficient. This section needs a more rigorous explanation of the specific problem with combination tables.
   
   - **Contribution 3:** The authors discuss this in Section 5 (lines 502-519), but the proof is unclear. For example, it's unclear how the two theorems prove "using non-vector feature embedding to avoid oversmoothing". Additionally there lacks empirical studies to support it. The theoretical justification for using non-vector embeddings to avoid oversmoothing is not well-established. The connection between the theorems presented and the claim that non-vector embeddings prevent oversmoothing is not clearly explained. Furthermore, the lack of empirical evidence makes it difficult to assess the practical significance of this theoretical argument.

### Questions
1. Are the phenomena described in Section 4.1 distinct from typical out-of-distribution scenarios?

2. In Section 5 (lines 502-519), what is the relationship between using (non-)vector feature embeddings and output embeddings being points?

3. Given that symbolic approaches are effective for syllogistic reasoning, why is it necessary for neural models to also support rigorous reasoning? In Section 2.1 (line 181), the authors argue that "symbolic approaches neither explain how symbols emerge from our neural minds nor capture the ways humans reason in daily life." Can neural models genuinely achieve these objectives?

### Soundness
2

### Presentation
3

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
The paper discusses the "dual-process" theory of mind, highlighting the distinction between fast, intuitive thinking  and slower, more deliberate thinking. It conclude that LLMs and
Foundation Models built upon Transformers cannot reach the rigour of syllogistic
reasoning. 
The article proposes a method of transforming syllogistic relationships into "part-whole relationships" and suggests using non-vector embeddings instead of traditional vector embeddings to avoid the problem of "oversmoothing." Oversmoothing can cause the outputs of neural networks to converge to similar embeddings, thereby affecting the accuracy of reasoning.

### Strengths
This paper attempts to analyze and study the reasoning capabilities of transformers, which is of great value. Additionally, the methods proposed in this paper possess certain innovative and theoretical significance.

### Weaknesses
1. This work lacks experimental validation and seems to be not fully complete.

2. The article is not clearly written. The abstract and introduction are somewhat verbose, and the key innovations and objectives are not clearly defined.

### Questions
In fact, enhancing the inference capabilities of neural networks is a very challenging task. Will merely changing traditional vector embeddings yield significant improvements, or can it lead to substantial advancements?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors study whether current neural networks can perform robust syllogistic reasoning via Euler diagrams, showing that they fail in very specific aspects, and conclude with arguments stating that neural networks need to go beyond vector embeddings to solve rigorous reasoning.

### Strengths
The paper is fairly well written, with some clear figures, especially in the revision. It presents multiple interesting ideas and experiments on syllogistic reasoning, a simple but easy-to-study problem.

### Weaknesses
I found it hard to follow what the contributions of this paper are. There are a few results that seem simple, arbitrary, poorly explained, and relevant only to a single network architecture. It is not clear to me what I should take home from these experiments. 

The 'sketched proof' which is supposed to prove that transformers cannot do syllogistic reasoning also falls short: It assumes that they oversmooth, which only happens for transformers with many layers (the theoretical results are for the infinite-depth setting). If this happened consistently in practical transformer models, there is no chance LLMs could work as well as they do (as also Dovonon 2024 argues and shows, which is cited). 

Together, this paper only provides meagre evidence for the infeasibility of syllogistic reasoning. Then the authors argue that different concept embeddings are needed, but do not compare (either theoretically or empirically) to the vector case, except for referring quickly to related work.

- What is the motivation for specifically studying this Siamese Masked Autoencoder model? I suppose that this model does not use specific embeddings for each object (unlike models in object-centric learning, involving eg slot attention [1] or the method specific for this task as cited [2])
- Line 357: "We fed new randomly generated test data' How is this data different?
- Line 359: What's the motivation for Euler Net version 2? The description of this method is extremely difficult to follow and incomplete. How does a model 'generate' input images?
- 4.1, first paragraph. This lacks in details. Furthermore, it's well known that standard NNs are not adversarially robust. This connection is missing. 
- 4.2: I did not understand the point of this experiment. Of course a model will not be able to say anything meaningful about incorrect input data that we never defined how to respond to, especially if it's not designed for out of distribution detection. 
- Line 428: This blanket statement is highly overclaiming these results. This is about misspecification - not a lack of learning capability. 
- 4.3: It is not clear to me how these combination tables are defined from a neural network point of view. Furthermore, this result again comes from the design of the neural network. If it's allowed to output multiple answers (for instance like an LLM would be able to), it may give all syllogistic conclusions. 
- 479 "More powerful than vanilla RNN, LSTM": From a theoretical perspective, this is hard to claim. RNNs (with unbounded time) are Turing Complete [3]. Similar results exist for Transformers, but these require an infinite 'scratchpad / chain of thought' [4]. I suppose this 'powerful' refers to an empirical interpretation, but this should be clarified. 
- Theorem 1 is unclear and informal, and does not properly state its assumptions. What is oversmoothing? Output embeddings? "will be points"? Of course output embeddings are points. What are the assumptions on the model architecture? A quick look at the proof did not help me understand these questions. This certainly doesn't constitute a 'rigorous proof" (Line 531)
- Similarly for Theorem 2, I have no idea what "If the output embeddings are not points" would mean.

### Questions
- What is the motivation for specifically studying this Siamese Masked Autoencoder model? I suppose that this model does not use specific embeddings for each object (unlike models in object-centric learning, involving eg slot attention [1] or the method specific for this task as cited [2])
- Line 357: "We fed new randomly generated test data' How is this data different?
- Line 359: What's the motivation for Euler Net version 2? The description of this method is extremely difficult to follow and incomplete. How does a model 'generate' input images?
- 4.1, first paragraph. This lacks in details. Furthermore, it's well known that standard NNs are not adversarially robust. This connection is missing. 
- 4.2: I did not understand the point of this experiment. Of course a model will not be able to say anything meaningful about incorrect input data that we never defined how to respond to, especially if it's not designed for out of distribution detection. 
- Line 428: This blanket statement is highly overclaiming these results. This is about misspecification - not a lack of learning capability. 
- 4.3: It is not clear to me how these combination tables are defined from a neural network point of view. Furthermore, this result again comes from the design of the neural network. If it's allowed to output multiple answers (for instance like an LLM would be able to), it may give all syllogistic conclusions. 
- 479 "More powerful than vanilla RNN, LSTM": From a theoretical perspective, this is hard to claim. RNNs (with unbounded time) are Turing Complete [3]. Similar results exist for Transformers, but these require an infinite 'scratchpad / chain of thought' [4]. I suppose this 'powerful' refers to an empirical interpretation, but this should be clarified. 
- Theorem 1 is unclear and informal, and does not properly state its assumptions. What is oversmoothing? Output embeddings? "will be points"? Of course output embeddings are points. What are the assumptions on the model architecture? A quick look at the proof did not help me understand these questions. This certainly doesn't constitute a 'rigorous proof" (Line 531)
- Similarly for Theorem 2, I have no idea what "If the output embeddings are not points" would mean. 

[1] Locatello, Francesco, et al. "Object-centric learning with slot attention." Advances in neural information processing systems 33 (2020): 11525-11538.

[2] Wang, Duo, Mateja Jamnik, and Pietro Lio. "Abstract diagrammatic reasoning with multiplex graph networks." arXiv preprint arXiv:2006.11197 (2020).

[3] Nowak, Franz, et al. "On the representational capacity of recurrent neural language models." arXiv preprint arXiv:2310.12942 (2023).

[4] Lena Strobl, William Merrill, Gail Weiss, David Chiang, Dana Angluin; What Formal Languages Can Transformers Express? A Survey. Transactions of the Association for Computational Linguistics 2024; 12 543–561.

### Soundness
1

### Presentation
2

### Contribution
2
