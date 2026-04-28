# Teaching LLMs How To Learn with Contextual Fine-Tuning

- Decision: Accept
- Avg Score: 6.75
- Scores: 5, 6, 8, 8

## Abstract
Prompting Large Language Models (LLMs), or providing context on the expected model of operation, is an effective way to steer the outputs of such models to satisfy human desiderata after they have been trained. But in rapidly evolving domains, there is often need to fine-tune LLMs to improve either the kind of knowledge in their memory or their abilities to perform open ended reasoning in new domains. When human's learn new concepts, we often do so by linking the new material that we are studying to concepts we have already learned before. To that end, we ask, "can prompting help us teach LLMs how to learn". In this work, we study a novel generalization of instruction tuning, called contextual fine-tuning, to fine-tune LLMs. Our method leverages instructional prompts designed to mimic human cognitive strategies in learning and problem-solving to guide the learning process during training, aiming to improve the model’s interpretation and understanding of domain-specific knowledge. We empirically demonstrate that this simple yet effective modification improves the ability of LLMs to be fine-tuned rapidly on new datasets both within the medical and financial domains.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents "Contextual Fine-Tuning" (CFT), a new approach for fine-tuning large language models (LLMs) that incorporates contextual prompts during training. These prompts, designed to mimic cognitive strategies like critical thinking and concept linking, aim to enhance the model's understanding and adaptability in domain-specific tasks, such as finance and medicine.

### Strengths
The paper introduces "Contextual Fine-Tuning" (CFT) as an extension of instruction fine-tuning to improve domain-specific learning, which is well-positioned to address limitations in traditional methods.

Extensive experiments demonstrate that CFT improves LLM performance on real-world datasets in domains like finance and medicine. The method yields notable improvements over continued pretraining (CPT) and instruction fine-tuning (IFT).

### Weaknesses
I wonder how fine-tuning on a specific domain impacts the language model’s general abilities. The authors could evaluate this by testing the model on general benchmarks to assess if base knowledge and instruction-following abilities are retained or diminished after domain-specific training. This would provide insight into whether contextual fine-tuning maintains the model's versatility across tasks.

### Questions
See the weakness part.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper examines the role of prompting in effectively fine-tuning LLMs for new domains. Based on the premise that prompting can play a decisive role at inference time, this paper proposes the contextual fine-tuning approach by which an additional context prompt prefix is added before fine-tuning/continual pertaining documents. These contextual prompt prefixes are designed based off of human educational theories and the present 5 such examples in their work. In a synthetic function approximation setting, they perform some illustrative experiments demonstrating that the choice of fine-tuning prompt can significantly impact whether new functions can be added in post-pretraining. In this setting, they also introduce an ablative method, negative contextual fine-tuning in which the model is given random information in the context prefix and they show that this performs wors. They then examine a real domain adaptive setting, involving fine-tuning an LLM on medical and financial data. They demonstrate that their method performs better than existing approaches such as continual pertaining, instruction fine-tuning, and their combination. They also show that a "negative contextual prompt" which suggests that the provided information might be incorrect performs worse.

### Strengths
Overall this paper does examine an interesting and important problem of expanding the knowledge or capabilities of a pre-trained large language model on new domains or topics. They propose a surprising source of gains: simply adding a prompt prefix to domain-relevant documents can improve the data efficiency of learning these new domains. The experiments across two domains appear to be well-designed and show some gains. As they note in their paper, the additional annotation and computational burden of this method is seemingly non-existent, and it could be flexibly combined with many existing continual pre-training corpora and techniques. The also attempt to justify the sources of their gains using a synthetic function-approximation task and demonstrate how an additional context can  result in faster learning. Overall, this analysis is somewhat interesting and also seems well thought out. The paper is in general easy to read and understand.

### Weaknesses
One major concern is the relationship between the synthetic setup and the real-world instantiation is not well-explained and seems somewhat tenuous to me. From my reading of the paper, it appears that the only major similarity is that both methods involve adding additional tokens to the "fine-tuning" documents (the contextual prompts in the real-world setting and the "original function evaluations" in the synthetic setting. However, these seem structurally different to me: in the synthetic setting, the added context tokens actually depend on the specific inputs and functions used in the example. On the other hand, in the real-world setting, the additional context tokens are sourced from the educational prompts and randomly sampled without considering he contents of a particular example. To summarize, it appears to me that contextual fine-tuning in the synthetic experiments actually provides a significant source of additional supervision (reminiscent of COT approaches) whereas this is absent in real-world instantiation of contextual FT. This makes the connection between the synthetic and real settings somewhat dubious to me and the mechanisms behind the contextual FT remain a bit mysterious. 

I also find that the design of the contextual FT prompts used in the real scenario is insufficiently justified. Currently, these prompts are associated with various educational theories. However, to me this appears to be insufficient justification because it is unclear -- and unlikely-- that any parallels can be drawn between the human learning process and the way that large language models use facts. Furthermore, if I understand the paper correctly, it seems that there is no actual task supervision corresponding to these contextual prompts (i.e. for the critical analysis prompt: "Critically analyze the upcoming information. Look for underlying assumptions, evaluate
arguments, and consider different perspectives.”, there is no actual ground-truth supervision given to the model on what the underlying assumptions/arguments in the provided information are). As a result, the mechanisms behind how these contextual prompts actually improve performance are quite unclear, and as I mentioned previously the synthetic data setup is not convincing in its relation to the real data setup. 

My concern is further amplified by the insufficient ablation analysis done on the contents of the "contextual prompts". The authors claim that the contents of the prompt are important by their "negative context fine-tuning setup". However, I think that the paper could be further strengthened if they expanded their analysis to non-contradicting context prompts which *are not* inspired by educational theories. This would help me assess the justification of the context prompt design and better understand the source behind the gains.

### Questions
1. I would like to see some additional ablations about the contents of the context prompts that go beyond the negative CFT setup. In particular, it would be nice if authors considered prompts consisting of various writing styles (but which are not correlated to educational theories or contradiction of the documents). This could help relate this work to prior research on the personas hypothesis etc. 
2. I would like if the authors could further justify how the synthetic data setup should be viewed as comparable to the real-world setup. In particular, why are the additional tokens added in the synthetic settings input dependent while the contextual prompts used in real settings are randomly sampled independently of the contents of the document/example?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces Contextual Fine-Tuning (CFT) for enhancing LLMs' learning capabilities by incorporating educational cognitive strategies during training. The key innovation is using instructional prompts designed to mimic human learning approaches, guiding the model's semantic understanding and domain-specific knowledge acquisition. The authors demonstrate CFT's effectiveness through experiments in medical and financial domains, showing improved performance compared to standard fine-tuning approaches while requiring limited training data.

### Strengths
- A novel contextual fine-tuning framework that combines in-context learning with gradient-based learning using educational psychology-inspired prompts
- Theoretical and empirical analysis demonstrating how contextual prompts affect model learning using synthetic experiments with simplified models
- Creation and curation of OpenMedText dataset, combining academic medical journals and textbooks, offering diverse training material
- Improved performance across down-stream applications, including medical and financial domains

### Weaknesses
 - For the experimental settings, the main experiments focus on comparison between CFT and CPT. To demonstrate the effectiveness, shall the comparisons also include other ICL methods, also RAG-based methods?
- While the authors provide thoughtful prompts based on educational theories in Appendix B1, it seems to be very limited exploration of prompt optimization or automated prompt generation methods, as the prompt template seems very various and task-specific.
- It might be beneficial to include computational cost etc. for efficiency evaluation. 
- While OpenMedText is a comprehensive dataset proposed in a research paper (not dataset/benchmark papers), more information regarding statistics, potential biases, quality issues etc. in the dataset are not thoroughly discussed.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a new technique, "contextual fine-tuning," which is designed to enhance fine-tuning of LLMs. The core idea is to prepend special text suggesting that the reader engage in deeper ways with upcoming content. The authors provide experimental evidence meant to show that the idea works in both synthetic and realistic settings.

### Strengths
The paper presents a very simple and intriguing idea for enhancing fine-tuning: prepending a prompt asking the reader to engage deeply with upcoming content.Moreover, experimental evidence from two real-world domains indicates that this technique outperforms natural baselines in several cases.

At a practical level, the experimental results are quite promising. This technique would be extremely easy to implement, so even small improvements with it would be a win. Although the experimental data indicates that the new method  ("Contextual Fine-Tuning" or CFT) is not always a win over the baseline over simply continued pretraining, it does seem to produce better results in many cases. Overall, I appreciated the medical and financial domain experiments, which seemed to have an appropriate level of complexity and realism to be a good test of the method.

At a theoretical level, this is certainly interesting. I find it counterintuitive that this technique works at all: one would think that the best way for the system to do next-token prediction would be simply to ignore the prepended CFT prompt, since it has no direct connection with the upcoming text. The fact that CFT produces good results is a hint that something surprising is happening under the hood, which could lead to future theoretical advances. Moreover, establishing that prepending this type of prompt is useful seems to point to many future areas of investigation for prepending other types of prompts.

UPDATE: In light of the new experiments, I have raised my score.

### Weaknesses
There is one major weakness in the paper: I am not at all convinced by Section 4. However, I think the best thing is for the authors simply to cut this section, because I actually don't think it's necessary for their argument.

Here's why I don't think Section 4 is relevant. In the synthetic function setting, the prepended prompts contain customized relevant information for the subsequent prediction tasks, helpfully factoring the functions that the system is learning to compute. This contrasts with the real-world CFT case, where—if I understand correctly—the prepended prompt has no customized connection at all to the upcoming text. I am happy to be corrected if I'm mistaken on this difference, but if I'm reading correctly, I think the synthetic task just doesn't shed light on the real-world task. That said, I don't think the synthetic task is particularly necessary for the argument, so I recommend simply cutting this section completely.

In addition to this major weakness, there are some aspects of exposition I'd try to improve. The first paragraph of the intro seems unnecessarily "hype-y." I actually think you could cut this paragraph and the paper would be fine. Also in the abstract and intro, I would say it's not clear to me that this method is necessarily "learning to learn": that might be one explanation, but there may be others. In the conclusion, the two paragraphs seem to repeat each other a bit. The authors might consider cutting the first one and just keeping the second. I also think it might be interesting for the authors, at some point, to speculate a bit on the mechanisms that make the technique work, or suggest some future experiments that might elucidate these mechanisms.

Typos: "human's" in abstract; "differes" and "initiial" around line 245.

### Questions
My main question is whether my reading of the difference between the synthetic vs. the real-world setting is correct. If the real-world prompts contain customized information about the upcoming text (contrary to my reading), then I would say Section 4 is relevant after all.

### Soundness
3

### Presentation
3

### Contribution
3
