# LOLAMEME: LOGIC, LANGUAGE, MEMORY, MECHANISTIC FRAMEWORK

- Decision: Reject
- Scores: 3, 3, 3

## Abstract
The performance of Large Language Models has achieved superhuman breadth with unprecedented depth. At the same time, the language models are mostly black box models and the underlying mechanisms for performance have been evaluated using synthetic or mechanistic schemes. We extend current mechanistic schemes to incorporate Logic, memory, and nuances of Language such as latent structure. The proposed framework is called \name\ and we provide two instantiations of \name: LoLa and MeMe languages. We then consider two generative language model architectures: transformer-based GPT-2 and convolution-based Hyena. We propose the hybrid architecture \nameA\ and use \name\  framework is used to compare three architectures. \nameA\ outperforms GPT-2 and Hyena on select tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This article introduces a novel framework called LOLAMEME that expands current mechanistic schemes to incorporate Logic, memory, and nuanced aspects of Language, such as latent structure. By using this framework, the authors compare three generative language model architectures: GPT-2 (transformer-based), Hyena (convolution-based), and proposed hybrid architecture T HEX which are constructed by replacing certain layer of the Hyena model with the GPT-2 layer. To instantiate LOLAMEME, the authors introduce two different manifestations, LoLa and MeMe, and evaluate the performance of the architectures across various aspects of language. The findings demonstrate that T HEX surpasses GPT-2 and Hyena on select tasks as well as a related benchmark dataset.

### Strengths
This work proposes a new hybrid architecture based on transformer-based GPT-2 and convolution-based Hyena. Experiments demonstrate the superiority of this architecture.

### Weaknesses
•	The motivation and problem formulation of this work is unclear. And the novelty and contribution of this paper are somewhat limited. The proposed new architectures are simply constructed by replacing certain layers of the Hyena model with the GPT-2 layer. Although some experiments demonstrate better performance on the proposed two test datasets, there may be a lack of validation experiments on other existing datasets. Additionally, providing some interesting findings or interpretations about the experiments through a deeper analysis of the proposed architectures should be better.
•	The construction procedure of the two datasets should be explained more clearly, and deeper consideration should be given to whether the experimental settings can reliably reflect the behavior of the related models, such as memorization and in-context learning.
•	There are quite a few typo errors, including grammar and table issues, in this paper. For example, in the abstract, it states "We propose the hybrid architecture T HEX and use LOLAMEME framework is used to compare three architectures." There are also typo errors in tables 3, 4, and 5. The grammar, figures, and tables in this paper may require some polishing.
•	The related work on mechanistic interpretability is not comprehensive. In fact, there is a considerable amount of work such as [1], [2], [3] attempting to interpret and understand the mechanisms of LLMs.
•	In section 6.5, it is unclear why TH EX-11 to T HEX-15 showed a loss of 0 after a few epochs but showed an exact match of 0. Further clarification or explanation is needed for this inconsistency.

### Questions
Please see the weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper talks a lot about mechanistic interpretability and evaluation of models with different architectures on synthetic benchmarks to generate more understanding of how they work. I fail to understand completely what insight is gained here.

### Strengths
.

### Weaknesses
The only changes done to the transformer architecture is to replace a single layer by a layer from the hyena model. The variations include only replacing a different layer of the transformer with the same hyena layer. Lots of experiments are done to compare the performance of variants and measure the impact on the quality under different input lengths, on some synthetic datasets, etc. But I don't see any insight that could be won from these experiments.

### Questions
None.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel framework called LOLAMEME including two instantiations, the LoLa language, and MeMe languages. Then it introduces a hybrid architecture T HEX and compares it with transformer-based GPT-2 and convolution-based Hyena based on the LOLAMEME framework. Furthermore, this work conducts comprehensive experiments to demonstrate the effectiveness of T HEX in different tasks.

### Strengths
1. The new framework LOLAMEME similar to natural language is impressive and interesting.
2. This work builds multiple datasets with several billion tokens based on the LOLAMEME framework, which would contribute to future research.
3. This work performs comprehensive experiments over these datasets and a related benchmark dataset to show the effectiveness of the new framework.

### Weaknesses
1. The motivation for the model design is not clearly discussed in this work. I am confused about the differences among T HEX, GPT-2, and Hyena. Specifically, the paper lacks a detailed explanation of why the T-HEX architecture, which combines attention and Hyena operators, was chosen over other possible hybrid architectures. The rationale behind selecting a single layer of attention within the Hyena framework is not well-justified, leaving the reader to wonder about the specific benefits of this particular configuration. A more thorough discussion of the design choices, including an analysis of the potential trade-offs, is needed.
2. The structure of this paper is not clear enough, which is very hard to follow. The flow of ideas is disjointed, making it difficult to understand the logical progression from the LOLAMEME framework to the T-HEX architecture and the experimental results. The paper jumps between concepts without clear transitions, and the organization of sections does not seem to follow a logical order. This lack of clarity significantly hinders the reader's ability to grasp the core contributions of the work.
3. I would suggest that an illustration figure be provided to clearly show the main idea of the LOLAMEME framework, which will make this work easier to understand. The abstract nature of the LOLAMEME framework makes it difficult to visualize, and a diagram could greatly enhance understanding. Without a visual aid, it is hard to grasp the relationships between the LoLa and MeMe languages and how they contribute to the overall framework. A clear illustration would clarify the framework's components and their interactions.
4. Some sentences should be revised and the format should be unified. For instance, in the Abstract, "We extend current mechanistic schemes to incorporate Logic, memory, and nuances of Language such as latent structure", I am curious why the first letter of Logic and Language in this sentence are capitalized. There are other instances of inconsistent formatting and phrasing throughout the paper, which distract from the technical content. The writing needs to be more precise and consistent to ensure clarity.

### Questions
1. What are the differences among T HEX, GPT-2, and Hyena? 
2. What are the advantages of T HEX? 
3. Why not provide an illustration figure to show the model framework?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
