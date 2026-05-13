# CogDevelop2K: Reversed Cognitive Development in Multi-modal Large Language Models

- Decision: Reject
- Scores: 5, 5, 3, 6

## Abstract
Are Multi-modal Large Language Models (MLLMs) stochastic parrots? Do they genuinely understand? This paper aims to explore the core cognitive abilities that human intelligence builds upon to perceive, comprehend, and reason in MLLMs. To this end, we propose \textbf{CogDevelop2K}, a comprehensive benchmark that spans 12 sub-concepts from primitive knowledge like object permanence and boundary to more complex abilities like intentionality understanding, structured via the developmental trajectory of a human mind. We evaluate 46 MLLMs on our benchmarks. Surprisingly, we observe a \textbf{reversed} cognitive developmental trajectory compared to humans. Comprehensively, we further evaluate the influence of evaluation strategies and prompting techniques.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper tries to develop a new dataset that helps answer whether LLMs are stochastic parrots. The authors construct a set of multimodal question-answering tasks grouped by cognitive development stages to evaluate Multimodal LLMs’ core cognitive capabilities. The dataset consists of single and multiple frame questions. The authors tested 46 MLLMs on the proposed benchmark and found that the MLLMs have a reversed cognitive development trajectory.

### Strengths
- The dataset consists of a diverse set of cognitive tests that can be beneficial to the community.
- This paper tests the benchmark extensively on different models and prompting techniques.
- The description of the paper is clear and easy to follow.

### Weaknesses
 - While it is an interesting dataset for evaluating MLLMs, a poor performance on this dataset doesn’t indicate whether LLMs are stochastic parrots. For example, LLMs are not required to have the ability in the sensorimotor stage to answer questions about object relationships. Specifically, the tasks designed for the sensorimotor stage, such as object permanence and spatial relationships, may not be fundamental requirements for achieving higher-level cognitive abilities in the context of MLLMs. The ability to perform well on tasks related to formal operations, such as abstract reasoning and hypothetical thinking, might stem from different mechanisms or training data biases, rather than a hierarchical dependence on sensorimotor skills.
- MLLMs perform better for questions in the Formal Operation stage may not be a reverse cognitive development trajectory. It can be related to the training data available for training MLLMs, most of them are in the later stage. So, it will be more beneficial to the community to understand why we need to know the cognitive development trajectory for MLLMs. The current analysis does not sufficiently explore alternative explanations for the observed performance patterns, such as the impact of pre-training data biases or the specific architectures of the MLLMs. The paper should delve deeper into the potential reasons behind the observed 'reverse' trajectory, rather than solely attributing it to a lack of core cognitive abilities. It would be beneficial to investigate whether the models are exploiting superficial patterns or shortcuts in the data, rather than demonstrating genuine understanding of the underlying concepts.

### Questions
- There are some other benchmarks inspired by cognitive reasoning. How does the proposed work relates or differs from those work? For example,
Shu, T., et al. "AGENT: A benchmark for core psychological reasoning. In ICML 2021.

### Soundness
2

### Presentation
3

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
This paper presents CogDevelop2K, a benchmark designed to evaluate cognitive development in multimodal large language models (MLLMs) using stages derived from Piaget’s theory of cognitive development. The authors examine the ability of 46 MLLMs to perform tasks associated with cognitive stages—sensorimotor, preoperational, concrete operational, and formal operational—using visual and textual information. Their results suggest an intriguing yet unexpected “reverse cognitive trajectory,” where MLLMs perform better on complex, abstract tasks than on simpler, foundational ones.

### Strengths
The paper’s strength lies in its novel attempt to frame LLM evaluation within Piaget’s developmental theory. This approach is relatively under-explored and introduces an interesting perspective for assessing MLLMs. Specifically, the work highlights cognitive aspects, such as object permanence and intentionality, that MLLMs often struggle with, even though they excel in other domains.

### Weaknesses
Despite its ambitions, the paper demonstrates significant limitations. While the authors claim to follow Piaget’s theory, their analysis predominantly relies on measuring sensor-based performance without adequately accounting for the motor and operational aspects critical to Piaget’s framework. This narrow focus restricts the evaluation to text-image understanding, excluding the interactive and embodied dimensions integral to cognitive development, which Piaget considered essential. Though I understand the MLLMs are currently only capable on text and image.

Furthermore, from a practical perspective, the selected benchmarks and developmental concepts provide little insight into the utility of LLMs in real-world applications. Large language models are typically designed for language-based interactions and problem-solving, not to replicate human-like developmental stages. The paper overlooks the fact that LLMs do not need proficiency in these specific developmental tasks to fulfill their primary functions effectively.

Finally, the evaluation results reveal limited takeaways. The findings reiterate known limitations—such as MLLMs’ reliance on pattern recognition over genuine understanding—without offering new pathways for advancing MLLM performance. The observed “reversed developmental trajectory” is an interesting phenomenon, but the analysis falls short of explaining its implications or translating it into practical guidance for AI development.

### Questions
The authors might want to consider answering questions and comments raised above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a new benchmark called CogDevelop2K, which presents visual reasoning questions that correspond to what the authors identify as different stages of human cognitive development.  The authors test both humans and multimodal LLMs on these questions and find that multimodal LLMs are better on questions corresponding to later stages of human cognitive development than they are on questions corresponding to earlier stages.

### Strengths
The paper divides evaluation into several dimensions that correspond to concepts associated with different developmental stages.  These include spatial reasoning, perceptual constancy, object permanence, temporal understanding and many others.  The dataset includes questions that use both single image frames and videos.  It is interesting, though not surprising, to see that Moravec's famous paradox holds here -- the tasks that are easier for LLMs are the ones that humans only accomplish at later developmental stages.

### Weaknesses
The paper's description of the developmental psychology literature seems outdated.  Most of the references to this literature are decades old, and there are few more recent references.  I'm not an expert on developmental psych, but I do know that there has been a lot of research in recent years that calls into question some earlier "accepted" results of, say, Piaget and others, even those working in the 1980s and 1990s.  The authors should cite more recent work here, and perhaps revise some of their claims about developmental stages accordingly.

The paper's main claim is stated in a way that I think is misleading: "we find an inverse cognitive developmental trajectory compared to humans".  This implies that LLMs "develop" along a "trajectory" that is the reverse of humans.  But of course LLMs do not develop along a trajectory (unless one wants to look at scaling trends or at models at different training checkpoints).  What's shown here is not a developmental trajectory, but rather a difference in what LLMs and humans find difficult, at different points in development for *humans*.  This should be made clearer as the central claim.  And perhaps reference Moravec's paradox.

The paper lacks some important references.  The authors state "we curate the first-ever vision cognitive development benchmark".  Other researchers have created AI benchmarks based on developmental psychology -- see e.g., https://arxiv.org/html/2406.10215v1 -- and on capacities that are part of the CogDevelop2K benchmark, e.g., physical reasoning (e.g., https://arxiv.org/pdf/2402.06119) and others.   The authors should be clearer on what their benchmark contributes, beyond the many "visual commonsense" benchmarks (e.g., https://visualcommonsense.com/) Also, there are many papers that investigate limitations of MMLMs on visual reasoning, and some of these should be cited.  

There are many things in the paper that were unclear, which I ask about in the Questions section below.  There are also numerous grammatical errors and typos -- the paper should be carefully proofread.

### Questions
How were the questions for the benchmark created?  Did the authors come up with questions related to the different evaluation dimensiona and then search for images / videos to use for those questions?  Or was it some other process? 

Will there be a link in the paper for downloading the benchmark?  

The paper states: "For a question to pass the screening stage, a minimum correctness of 95% was required from both reviewers."  I didn't understand this -- what does "95% correctness" mean for a single question?  

The paper states: "current interleaved image understanding and video understanding models cannot be effectively compared on the same question."  What does "interleaved image understanding and video understanding" mean?  [I don't know what you mean by "interleaved" here.]  And why can't current models be compared on the same question? 

I also am not sure what you mean by "interleaved image-text datasets" and "multi-video interleaving and video-image interleave formats".  

I really did not understand the description of the "Human Benchmark".  You say that there were 22 participants.  Then you say "Each annotator was asked to label 2 to 6 concepts".  Are the 22 participants acting as labelers, or as participants answering questions from the dataset?  What are the human labels used for?  You also say "Participants were instructed to skip a question if the question is worded ambiguously or is too complicated to answer in 90 seconds".  Are these participants answering questions from the benchmark?  What happened to those questions that people skipped?  Were they taken out of the benchmark and not used for LLM evaluation?    All this needs much clearer explanation.  

Also, human performance is given in Figure 5.  How many humans were tested on each benchmark question?  How many benchmark questions were given to each human?  Say more about the human study -- how were they presented with the questions ? Were there questions given to LLMs that weren't given to humans?  Can you give some statistical significance measures to the differences between models and between humans and LLMs? 

Also, Figure 5 is very hard to read.  It would be useful if you just picked the five best models, and gave their accuracies compared to humans in a table, and put the rest of the results in an appendix.  Also, for the LLM results, which prompt format was being used?

The paper states that for the questions in the benchmark: "the textual information is highly relevant to but does not overlap the image content".  It would help to give an example, or point to one already in paper.

The paper states: "GPT families show moderate performance, with accuracy scores between 0.4 and 0.6".  For these and other results, what is random chance baseline? Why do you call this "moderate" performance? 

For Table 2,  What is the prompt in "empty string" condition  Just the question itself plus images?   Give an example of an actual prompt, including the question itself.  For all the prompt formats listed in Table 2, where does the prompt text go with respect to the question itself?

Also for Table 2: Are the values given in the table the accuracies over all questions in the dataset? 

Table 2: "Concept: [concept description]".  Give an example of a concept description that would appear here.  

"Concept explanation...surpasses all the other prompts by at least 6%". I'm confused by this.  GPT4o-High for example gets 0.636 with "explanation" prompt and "0.617 with "role assignment prompt."  This
is less than 3 percent difference.  There are other even closer examples in the table.  

The paper states, for Table 2: "We observe that most prompts are useful on our benchmark, increasing
the averaged performance by at least 1%." Increased over what?

"MMLMs virtually do not understand the answers they produce when tackling complex reasoning tasks".  On this you should cite https://arxiv.org/abs/2311.00059

"This study serves as a step toward unraveling the nature of MLMM intelligence and their potential limitations in mirroring human cognitive development."  But why should mirroring human cognitive
development be a goal?

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
4

### Summary
The paper investigates whether Multi-modal Large Language Models (MLLMs) truly understand the tasks they excel at or if they are simply mimicking intelligence by learning spurious correlations. The authors aim to answer whether MLLMs possess genuine cognitive capabilities akin to human intelligence or if they are “stochastic parrots” that predict outcomes based on statistical patterns rather than comprehension. To explore this, the authors propose a new benchmark called CogDevelop2K, inspired by human cognitive development. CogDevelop2K comprises 2,519 questions paired with 2,517 images and 455 videos. The authors used different prompting techniques to assess a large set of MLLM models under different conditions. For the final conclusion,  the authors observed a reversed cognitive
developmental trajectory compared to human beings.

### Strengths
- The paper tackles a pressing question in the rapid development of the MLLMs. From my point of view, CogDevelop2K is a novel and well-designed benchmark that comprehensively spans multiple cognitive domains. It includes a wide variety of tasks, from simple core concepts like object permanence to complex reasoning, making it a robust tool for evaluating the cognitive capabilities of MLLMs. Human cognitive development theories are well-studied, while MLLMs are not. By linking AI performance to human developmental stages, the study provides a unique perspective and a structured framework for evaluation.
- The experiments are well-designed and comprehensive, and the dataset is extensive. I think the paper provides a generally broad and varied evaluation of currently popular MLLM models, and offering a thorough comparison of existing models’ strengths and weaknesses across cognitive domains.

### Weaknesses
 - The study primarily focuses on the performance of MLLMs, which are heavily reliant on vast amounts of training data. This reliance raises questions about the models' true cognitive capabilities, as the impressive results may simply reflect the capacity to identify statistical correlations in massive datasets rather than genuine comprehension or understanding. It's difficult to determine if their cognitive abilities are a result of learning core principles or merely memorizing patterns. This limitation suggests that the current approach might not effectively distinguish between true intelligence and advanced pattern recognition. While I ack that the CogDevelop2K benchmark is an interesting contribution, the paper may not push the community forward in developing more sophisticated or truly intelligent AI systems from a technical view. 
- Lack technical contribution. The study lacks a detailed technical analysis, making its findings primarily observational. This limits its impact on advancing MLLM development, as it does not offer a clear path for addressing the identified limitations or enhancing the cognitive capabilities of AI systems. While the paper provides valuable insights into the current performance of models, it falls short of proposing technical insights that could drive meaningful progress in the field.
- Some typos, i.e., line 66 "CogDeveop2K".

### Questions
- What factors do you believe contribute to the reversed cognitive developmental trajectory observed in MLLMs? Is it a consequence of the models' training data, architecture, or inherent biases in the dataset?
- How well do you think the CogDevelop2K benchmark generalizes to the applications or the development of MLLMs? Are there specific use cases where you believe MLLMs' performance on this benchmark accurately reflects their capabilities? Based on the evaluation results, how the CogDevelop2K can help improve the development of MLLMs?

### Soundness
3

### Presentation
3

### Contribution
3
