# A Framework for Inference Inspired by Human Memory Mechanisms

- Decision: Accept
- Scores: 6, 6, 8

## Abstract
How humans and machines make sense of current inputs for relation reasoning and question-answering while putting the perceived information into context of our past memories, has been a challenging conundrum in cognitive science and artificial intelligence. Inspired by human brain's memory system and cognitive architectures, we propose a PMI framework that consists of perception, memory and inference components. Notably, the memory module comprises working and long-term memory, with the latter endowed with a higher-order structure to retain extensive and complex relational knowledge and experience. Through a differentiable competitive write access, current perceptions update working memory, which is later merged with long-term memory via outer product associations, reducing information conflicts and averting memory overflow.
In the inference module, relevant information is retrieved from two separate memory origins and associatively integrated to attain a more comprehensive and precise interpretation of current perceptions. We exploratively apply our PMI to improve prevailing Transformers and CNN models on question-answering tasks like bAbI-20k and Sort-of-CLEVR datasets, as well as detecting equilateral triangles, language modeling and image classification tasks, and in each case, our PMI enhancements consistently outshine their original counterparts significantly. Visualization analyses reveal that relational memory consolidation, along with the interaction and integration of information from diverse memory sources, substantially contributes to the model effectiveness on inference tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Inspired by human brain’s memory system and cognitive architectures,this paper propose a PMI framework that consists of perception, memory and inference components. Notably, the memory module comprises working and long-term memory, with the latter endowed with a higher-order structure to retain more accumulated knowledge and experiences. 


In my opinion, the motivation of this paper is meaningful because it comes from the human brain's memory. 
And the proposed memory module looks like powerful because it consists of working memory and long-term memory.
However, the experiments may not be enough due to it not compare with other memory augment models, such as the memory augment language model. and this paper not take experiments on language generative task.
Besides, the

### Strengths
1. The motivation is sometimes novel and comes from human's brain memory. 

2. The proposed model is meaningful with its novel motivation

3. The paper is well written, and the image is easy to understand.

### Weaknesses
1. the experiments may not be enough to compare it with other memory-assisted language model

2. The experiments is hard to understand, and i think it is not necessary to conduct experiments on image classification. And there is little work on the memory augment image model due to the image's too long context. 

3. I don't see any connection between your work and the title, the author maybe need change a title due to this model hard to help us underanding AI .

### Questions
No

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a cognitive framework called PMI that consists of perception, memory, and reasoning modules. It is inspired by human memory mechanisms and aims to improve the understanding and handling of relational questions in AI systems. The memory module includes working memory (WM) and long-term memory (LTM), with LTM having a higher-order structure to retain accumulated knowledge. Current perceptions update WM through competitive write access and are merged with LTM via outer product associations. The inference module retrieves relevant information from both WM and LTM to generate comprehensive insights. The PMI enhancements consistently outperform their original counterparts in tasks such as question-answering, relation calculation, and image classification.

### Strengths
- Integration of cognitive science and AI: The paper draws inspiration from multiple memory systems theory and global workspace theory in cognitive neuroscience, and applies these insights to develop the PMI framework for AI systems.

- Novel memory module: The PMI framework introduces a dual-layer memory block with distinct communion principles, featuring working memory (WM) and long-term memory (LTM). This structure allows for efficient information filtering, storage, and knowledge consolidation.

- Enhanced performance: The PMI enhancements consistently outperform their original counterparts in various tasks such as question-answering, and image classification. This demonstrates the effectiveness of the proposed framework in improving AI systems' understanding and reasoning abilities.

- Clear experimental results: The paper provides detailed experimental results, including accuracy rates and convergence rates, to support the effectiveness of the PMI module. Visualizations of attention patterns further illustrate the model's ability to consolidate and integrate information from different memory sources.

- Reproducibility: The authors plan to share their code once the review process is completed, ensuring the reproducibility of their experiments and allowing for further research and development in this area.

### Weaknesses
 - The text appears to be excessively embellished. I would like to encourage the author to employ conventional terminology, as exemplified by the authors referencing "relation calculation" in the abstract.

- The paper includes visualizations of attention patterns between perceptions and memories, but it could benefit from providing more detailed explanations and interpretations of these visualizations. 

- Examining the qualitative impact of your modules on various types of tasks would provide valuable insights, rather than solely relying on quantitative results. This approach would enhance the paper's overall credibility. You can achieve this by employing various visualization techniques and similar methods.

### Questions
Please see weaknesses above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work presents a novel architecture inspired by memory systems in cognitive science. The method improves performance across multiple reasoning tasks in both transformer and CNN architectures.

### Strengths
- The proposed architecture improves performance across a diverse set of reasoning tasks.
- A reasonable set of baseline comparisons are included.
- An ablation study is performed to assess the impact of specific components.

### Weaknesses
 - The primary limitation concerns the framing of the architecture as instantiating both working memory and longterm memory. It is not clear to me that the architecture actually involves longterm memory in any meaningful sense. I think the approach would be better described as a form of relational working memory (utilizing a tensor product to capture relational information). This of course doesn't concern the method itself, which seems to perform well across multiple tasks. But I think the contribution would be much more clearly framed as a kind of working memory that exploits *relational* information. The role of relations in working memory is very well-studied in cognitive science (see references below), and I think this would make an interesting topic for discussion.
- Is it possible to study an ablation model that includes the 'longterm' memory component but not the 'working' memory? It seems likely that the tensor product in the longterm memory component is primarily driving the gain in performance, and it would be nice if this could be isolated.
- It would be good to cite work from cognitive science on the role of tensor product representations in working memory [1,2] as this is highly related to the outer product mechanism in the 'longterm' memory module.

Minor comments:
- It sounds like what is referred to as the transformer baseline in this work is actually a 'universal transformer' [3] in which parameters are shared across layers, and what is referred to as a 'high capacity transformer' is just a standard transformer (in which each layer has different parameters).

### Questions
- In what sense does the 'longterm' memory module involve long term memory more than the 'working' memory module? They both seem to operate over the same timescale, the only difference being the presence of the tensor product to capture relational interactions (which is not related to longterm vs. working memory).
- Is it possible to ablate the 'working' memory module?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
