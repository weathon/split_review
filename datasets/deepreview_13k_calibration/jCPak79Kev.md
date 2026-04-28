# AnalogGenie: A Generative Engine for Automatic Discovery of Analog Circuit Topologies

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 6, 8, 8

## Abstract
The massive and large-scale design of foundational semiconductor integrated circuits (ICs) is crucial to sustaining the advancement of many emerging and future technologies, such as generative AI, 5G/6G, and quantum computing.
Excitingly, recent studies have shown the great capabilities of foundational models in expediting the design of digital ICs.
Yet, applying generative AI techniques to accelerate the design of analog ICs remains a significant challenge due to critical domain-specific issues, such as the lack of a comprehensive dataset and effective representation methods for analog circuits.
This paper proposes, $\textbf{AnalogGenie}$, a $\underline{\textbf{Gen}}$erat$\underline{\textbf{i}}$ve  $\underline{\textbf{e}}$ngine for automatic design/discovery of $\underline{\textbf{Analog}}$ circuit topologies--the most challenging and creative task in the conventional manual design flow of analog ICs.
AnalogGenie addresses two key gaps in the field: building a foundational comprehensive dataset of analog circuit topology and developing a scalable sequence-based graph representation universal to analog circuits.
Experimental results show the remarkable generation performance of AnalogGenie in broadening the variety of analog ICs, increasing the number of devices within a single design, and discovering unseen circuit topologies far beyond any prior arts.
Our work paves the way to transform the longstanding time-consuming manual design flow of analog ICs to an automatic and massive manner powered by generative AI.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces AnalogGenie, a generative tool to create analog circuit topology based on a generative model. The method has two contributions: first, the paper collects a large and complete analog circuit dataset; second, the scalable generation of analog circuits; the paper proposes to transfer the analog circuit into a sequence-based graph, thus enabling the usage of a generative model with token-based generation. With dataset augmentation and pre-training, AnalogGenie can finish 73.5% of problems, outperforming the best baseline with 68.2%.

### Strengths
Strength:
* The idea of transferring the analog circuit into a sequence-based graph representing is a novel and interesting idea, enabling the use of a generative model for scalable circuit generation.
* The collection of large-scale analog circuits. It would be great if the authors can release the dataset.

### Weaknesses
Weakness:
* The main weakness of this paper is that it only considers generating functional circuits, which limits its effectiveness.  In real-world tasks, analog designers need to optimize the topology based on the design targets, e.g., sizing. Does this work consider performance optimization during the generation process, or is it only considered functional? Have you performed sizing?

More weaknesses please check the questions:

* The paper tries to tackle a simple task with topology generation, but how can the more critical analog circuit structure selection and sizing problem be solved?
* Based on my understanding, the paper didn't propose methods to optimize circuits's FoM. Therefore, the paper shouldn't compare the FoM, as the benefits may come from your large dataset, and the model may reuse some circuits. This is unfair as previous methods cannot access the large dataset you have collected.
* For fine-tuning, how do you ensure the validation circuit has no overlapped knowledge in the fine-tuned dataset? More details about fine-tuning datasets should be included. Your fine-tuning significantly improves the accuracy. Is it because some structures are seen during training? Could you show some examples that, without fine-tuning, it fails, but after fine-tuning, it succeeds?
* Based on the definition of an Eulerian circuit that only visits edge once, but the example in appendix A.7 (Fig.7), the first generated sequence visit VOUT-PMI-G twice. Could you explain on why it is not consistent with your definition?

### Questions
Questions:
* To ensure the practicality of the designed circuit in real-world circuit design scenarios, the process technology of circuit fabrication should be taken into consideration. How do you think this current work can be extended to incorporate advanced process technologies and further optimize the design for improved performance and efficiency?
* Based on my understanding, the paper didn't propose methods to optimize circuits's FoM. Therefore, the paper shouldn't compare the FoM, as the benefits may come from your large dataset, and the model may reuse some circuits. This is unfair as previous methods cannot access the large dataset you have collected.
* The paper tries to tackle a simple task with topology generation, but how can the more critical analog circuit structure selection and sizing problem be solved?
* For fine-tuning, how do you ensure the validation circuit has no overlapped knowledge in the fine-tuned dataset? More details about fine-tuning datasets should be included. Your fine-tuning significantly improves the accuracy. Is it because some structures are seen during training? Could you show some examples that, without fine-tuning, it fails, but after fine-tuning, it succeeds?
* Based on the definition of an Eulerian circuit that only visits edge once, but the example in appendix A.7 (Fig.7), the first generated sequence visit VOUT-PMI-G twice. Could you explain on why it is not consistent with your definition?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors introduce a novel methodology for analog circuit design, leveraging the capabilities of generative AI (specifically, GPT-based models) alongside a fine-grained Directed Acyclic Graph (DAG) representation. Additionally, they present a new dataset tailored to this task, developed through data augmentation techniques.

### Strengths
1. The authors propose an innovative RAG representation for analog circuits, where each node corresponds to a device pin. This approach enables the model to capture low-level features and generate topologies in a fine-grained way.

2. The authors present a new open-source dataset that comprises LDOs, bandgap references, comparators, PLLs, LNAs, PAs, mixers, and VCOs. Unlike previous datasets, this dataset includes performance metrics for each circuit. To ensure accuracy, the researchers manually implemented each circuit in an industry-standard design tool and conducted simulations, which is a significant manual effort.

3. The authors avoid using adjacency matrices to represent circuit topologies. Instead, they employ an Eulerian graph representation, which effectively reduces the model’s memory requirements.

4. To the best of my knowledge, this is the first work to apply generative AI models to tasks in analog circuit design.

5. The authors employ data augmentation techniques by learning multiple unique Eulerian circuits that represent the same topology. This approach mitigates overfitting and reduces inductive bias, enhancing the model's generalization capability.

### Weaknesses
The experimental part over-emphasized the performance of the model itself. There is no data that shows the performance of the circuits generated by the AGI models. Since the generated circuits are about to be used in the real physical world, I think it is essential to analyze some basic and widely-used analog circuits like OpAmps(including the slew rate, GBW, CMRR, AoI, Ib, Vos, etc.), LDO(including Dropout Voltage, PSRR, etc.)

I am quite confused about the expression of inductive bias in graph-based data. In the paper, the authors pointed out that to address the inductive bias issue, the model learned multiple unique Eulerian circuits that represent the same topology. Do these Eulerian circuits have different or share the same inductive bias? Since I am not a researcher in graph neural networks, I hope the authors could give me detailed and easy-to-understand instructions to explain this issue (better include proofs)

To to best of my knowledge, the authors use pin-grained graph representation to describe a typical circuit design. Is this strategy a kind of data augmentation since a graph with more nodes can represent more information? If so, the main innovative point of this work is to change the representation to a lower level. If we apply such a strategy to other methods without using AGI models, will those older methods (Like GNN-based models) perform better as well?

In the real world, the demand for RF circuits is high and those devices require very strict performance and electrical parameters (like filters, PLL, etc.). Is this system fully qualified to handle such devices' circuit generation? If so, are the generated circuits' performance as good as or even better than those that already exist?

### Questions
1. I am quite confused about the expression of inductive bias in graph-based data. In the paper, the authors pointed out that to address the inductive bias issue, the model learned multiple unique Eulerian circuits that represent the same topology. Do these Eulerian circuits have different or share the same inductive bias? Since I am not a researcher in graph neural networks, I hope the authors could give me detailed and easy-to-understand instructions to explain this issue (better include proofs)

2. To to best of my knowledge, the authors use pin-grained graph representation to describe a typical circuit design. Is this strategy a kind of data augmentation since a graph with more nodes can represent more information? If so, the main innovative point of this work is to change the representation to a lower level. If we apply such a strategy to other methods without using AGI models, will those older methods (Like GNN-based models) perform better as well?

3. In the real world, the demand for RF circuits is high and those devices require very strict performance and electrical parameters (like filters, PLL, etc.). Is this system fully qualified to handle such devices' circuit generation? If so, are the generated circuits' performance as good as or even better than those that already exist?

### Soundness
3

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
This paper introduces "AnalogGenie," a new tool designed to automatically discover analog circuit topologies. The authors aim to tackle some of the biggest hurdles in automating analog IC design, like the lack of comprehensive datasets and effective ways to represent analog circuits.

The main focus here is on automating the design of analog ICs, which is notoriously tricky. Unlike digital ICs, analog circuits don't have a straightforward hierarchical structure and rely heavily on designer intuition and experience. This makes automation a real challenge, and that's exactly what this paper tries to address.

### Strengths
The authors reference several earlier efforts, like CktGNN, LaMAGIC, and AnalogCoder, that have explored using generative AI for analog circuit design. These prior works show promise, but there's still a lot of unexplored potential in this area.

AnalogGenie takes a novel approach by creating a large dataset of over 3,000 analog circuit topologies and developing a scalable sequence-based graph representation. They also introduce a customized tokenizer and a pre-training method that allows the model to learn from these topologies without needing to know specific performance metrics or circuit types.

While the paper doesn't dive into the nitty-gritty of the experiments, it does claim that AnalogGenie can produce a wide range of large-scale, valid, and high-performance analog circuit topologies, outperforming previous methods.

Overall, AnalogGenie seems like a promising step forward in the automation of analog circuit design. However, it would be great to see more detailed discussions on its limitations and how it stacks up against other state-of-the-art methods. More insights on future directions could also help guide further research in this exciting area.

### Weaknesses
One downside is that the paper doesn't really discuss any limitations of AnalogGenie or suggest areas for future research. It hints at a lot of untapped potential in the field of analog IC design automation and suggests that AnalogGenie's approach might even be applicable to digital design.

### Questions
The paper mentions the use of a customized tokenizer and a finetuning process for AnalogGenie. How do they help tailor AnalogGenie to the analog circuit design task and improve the generation quality? Additionally, will this custom tokenizer affect its performance on other tasks, potentially reducing the inherent reasoning ability of the language model? Are there any metrics or experimental methods that can be used to verify these issues?

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
5

### Summary
This paper makes a substantial contribution to the automation of analog integrated circuit design, an enduringly challenging problem in electronic design automation (EDA). It introduces a novel approach, establishing a unique, one-to-one mapping between a graph and the circuit topology. Here, each circuit connection is explicitly represented, requiring analog circuits to be modeled at the pin level. A key innovation is a method to transform the undirected graph into a sequence format. Following data augmentation, the authors train a GPT model that generates diverse analog circuits by predicting the next device pin connection within a circuit. The evaluation results demonstrate that the proposed GPT model significantly outperforms previous models.

The work is impressive, presenting AnalogGenie, a powerful GPT-based model capable of generating a much broader range of large-scale, valid, unseen, and high-performance analog circuit topologies than prior models. It also introduces an efficient, sequence-based, pin-level graph representation that effectively captures complex analog circuit structures. Additionally, the paper constructs a comprehensive, large-scale, high-quality dataset of analog circuit topologies, covering nearly all major categories, including RF circuits. This dataset will likely serve as a valuable resource for further advancements in analog circuit design automation.

### Strengths
This is a remarkable work with several innovative contributions. First, it introduces an efficient and precise pin-level graph representation of analog topologies, enabling a unique one-to-one mapping between the graph and the circuit topology. Second, the authors treat undirected edges as two directed arcs in opposite directions, ensuring that the graph contains at least one Eulerian circuit starting from any vertex. Using this approach, they can sequentialize the graph of an analog circuit into an Eulerian circuit—a trail that visits each edge exactly once and both starts and ends at the "VSS" node. Third, the work implements data augmentation by enumerating all possible trails, effectively reducing overfitting and enhancing the model's generalization ability. Fourth, by creatively applying techniques from natural language processing, the paper reframes analog topology generation as a next-device-pin prediction task, with "VSS" acting as the starting token.

Additionally, this work provides a comprehensive, high-quality, large-scale dataset, poised to greatly advance analog design automation. Thanks to these innovative aspects, AnalogGenie achieves state-of-the-art performance. As a reviewer with experience in analog circuit design during undergraduate studies, I find the circuits presented in the Appendix valuable and practically significant.

### Weaknesses
The dataset introduced in this work encompasses various types of analog circuits, though the experiments conducted focus primarily on commonly used analog circuits. While these circuit types—such as operational amplifiers, power converters, and bandgap references—are indeed foundational in analog electronics, I hope the authors will consider expanding their experiments to include additional analog circuit types in future work. For example, circuits like low-noise amplifiers (LNAs), mixers, and phase-locked loops (PLLs), which are crucial in RF and communication systems, are not explicitly addressed. Furthermore, I encourage the authors to present these well-designed circuits to senior engineers for evaluation and, if possible, pursue a tape-out to demonstrate real-world feasibility. The current evaluation, while showing promising results, lacks the validation from experienced analog designers and the confirmation of silicon implementation, which are critical for assessing the practical utility of the generated designs.

### Questions
1.The authors are committed to open-sourcing this, correct? It would be valuable if they honor that commitment, as their work, if as described, could greatly benefit the automation of analog circuit design.?
2.Can the authors explain how the sizing is done?

### Soundness
4

### Presentation
4

### Contribution
4
