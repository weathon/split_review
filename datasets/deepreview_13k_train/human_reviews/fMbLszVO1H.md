# LongMamba: Enhancing Mamba's Long-Context Capabilities via Training-Free Receptive Field Enlargement

- Decision: Accept
- Scores: 8, 5, 8, 6

## Abstract
Mamba models have emerged as an efficient alternative to Transformer models for language modeling tasks, offering linear complexity as context length increases. However, despite their efficiency in handling long contexts, recent studies have demonstrated that Mamba models underperform in understanding extended contexts compared to Transformer models. To address this significant shortfall, we propose ``LongMamba", a training-free technique that significantly enhances the long-context capabilities of Mamba models. Our approach builds upon the discovery that hidden state channels in Mamba models—categorized into \textit{local} and \textit{global channels} based on their receptive field lengths—exhibit distinct functionalities. Specifically, the \textit{global channels} struggle to adaptively extend their effective receptive fields when input lengths far exceed their training sequence length due to exponential decay in their hidden states. We hypothesize this exponential decay is the root cause of Mamba models’ limited performance in extended contexts. LongMamba counters this by effectively expanding the \textit{global channels}' receptive fields to fully encompass the input sequence length, thus enabling them to capture global information more effectively. Through extensive benchmarking across synthetic and real-world long-context scenarios, LongMamba sets a new standard for state-of-the-art performance in Mamba-based long-context tasks, significantly extending the operational range of Mamba models without requiring additional fine-tuning. All code and models will be released upon acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a simple modification to Mamba architecture where they prevent channels from exponential decaying by filtering out tokens from the training sequence if the update is small than threshold , for smaller updates and keepin them as is for larger updates. This allows to prevent catastrophic forgetting, and surprisingly allows to reuse existing model on a significantly longer context without finetuning. 
The modification seem pretty straightforward where they essentially identify "Global channels" that seem to be particularly prone to exponential decay and change the SSM update procedure to ignore some of the smaller update to reduce the amount of exponential decay for longer contexts.

### Strengths
The main result is very interesting: they show that existing SSM architectures acan be expanded to much longer contexts without having to fine tune it. Overall  a simple mechanism that seemingly enables Mamba to generalize to much longer contexts. Great introduction to Mamba models.

### Weaknesses
See questions. I think the empirical analysis section would benefit from some more detail study  of distribution of local vs global channels receptive field (see Q5 below). Sec 5 would benefit from expanding how A' are computed.

### Questions
1. End of Section 5: line 333, i think you meant Eq 16 not E 18?
2. It is not clear what A'_t are if updates is greater than threshold.  (e.g. dual of Eq 17)
3. How is g(S) computed? Is it computed to satisfy equation 16?
4. Local/Global channel: is the number 0-300-600-900-1200 are just percentiles of a fixed model? It would be better to specifically say that.
5. Can you include a graph showing the cumulative graph of receptive fields for each each channel? Especially this would be interesting for training seq.len and a much longer seq len?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces LongMamba, a method to extend the context length of Mamba models without additional training, focusing on long-context understanding for state-space models. Mamba models, though efficient in handling long contexts due to their linear complexity, struggle with context lengths far beyond training sequences due to exponential decay in the attention value, especially toward early tokens. LongMamba addresses this by categorizing channels into local and global based on receptive field lengths, then enlarging global channels' receptive fields via adaptive decay adjustments through token filtering. This modification allows LongMamba to maintain performance over long contexts without the computational cost of fine-tuning, making it a practical improvement over previous methods like DeciMamba.

### Strengths
1 - The paper addresses a critical challenge in long-context modeling, particularly for SSMs like Mamba, which suffer from limited long-sequence capabilities despite their efficient state-space mechanics. Enhancing this capability without retraining aligns well with real-world demands for scalable, efficient language models.


2 - Devising a “training-free” context extension technique is an important aspect of the paper, as directly training the SSMs on longer context requires significant compute/resource and expansive datasets. 


3 - Extensive benchmarks show that LongMamba consistently outperforms vanilla Mamba on long-context tasks, including language modeling on the PG-19 dataset and passkey/document retrieval. LongMamba’s results in real-world tasks, such as LongBench, also showcase its adaptability

### Weaknesses
1- A substantial limitation is that LongMamba relies heavily on the DeciMamba[1] framework, raising questions about its independent novelty. Although LongMamba innovatively extends global channels, the reliance on DeciMamba's token handling might limit its perceived originality. In particular, the idea of token filtering based on the averaged delta_t value was proposed by DeciMamba. LongMamba merely improves upon this idea by limiting the scope of this averaging to some specific channels (global channels).

2 -The paper does not systematically address threshold selection for distinguishing global versus local channels. This selection is left to empirical values, which may lack generalizability across different datasets or models. A more formal approach to tuning this threshold would strengthen LongMamba's applicability. This is of importance, as global and local channels are integral parts of the LongMamba framework.


3 - The method for handling global channels’ decay distribution adjustment is not fully elaborated. It remains ambiguous whether averaging across global channels fully mitigates decay issues over extended contexts, potentially affecting LongMamba’s consistency in varied contexts (Figure 2c, Decay Distribution Adjustment). It's unclear if the averaging is performed across all global channels, or if each channel is handled independently, which could lead to different interpretations of the method's efficacy.

### Questions
1. Could the authors please address the points mentioned in the weaknesses section?

2. Is a similar exponential decay observed in the Mamba2[2] model? If so, does LongMamba improve the long-context understanding in this architecture as well?

3. Would the proposed approach generalize to other SSMs beyond Mamba, including hybrid Transformer/SSM architectures, or is it specifically tailored to Mamba’s architectural nuances?

4. LongBench is a comprehensive benchmark. How does LongMamba perform on other LongBench tasks, namely 2wikimqa, TREC, TriviaQA, LCC, and RepoBench-P?

5. Have the authors considered alternative strategies for decay adjustment besides token filtering? If so, why was filtering chosen over other methods? 

References:

[1]Ben-Kish, Assaf, et al. "DeciMamba: Exploring the Length Extrapolation Potential of Mamba." arXiv preprint arXiv:2406.14528 (2024).

[2]Dao, Tri, and Albert Gu. "Transformers are SSMs: Generalized models and efficient algorithms through structured state space duality." arXiv preprint arXiv:2405.21060 (2024).

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces LongMamba, a training-free techniques to enhance Mamba model's ability to handle long sequences beyond the training context lenght.  

The authors discovered that Mamba's hidden state channels can be categorized into two types: local channels that focus on nearby context, and global channels that attend to the entire input sequence. 
The key limitation they identified is that global channels fails to be functional when processing sequences longer than the training length and they hypothesize the exponential decay is the root cause.   

To this end, they propsoe LongMamba that addresses this by enlarging receptive fields of global channels by filtering out the less important tokens while maintaining similar decay distributions as during training.
Through extensive experiments on tasks like Passkey Retrieval, Document Retrieval, Language Modeling, and LongBench, LongMamba shows promising result without additional training and outperform vanilla mamba and previous methods.

### Strengths
- The finding about the categroies of channels of Mamba models(local and global) is interesting and meaningful, which could bring insight to the community for better understanding the Mamba model's behavior.

- The experiment results are strong as it outperforms the vanilla Mamba model by large margin.

- This paper is well-written and easy to follow, for example, they reveal the "categroies of channels" phenomena with sufficient analysis and visualization and figure 2 (the method overview) is tidy and clear

### Weaknesses
The paper is generally good but I believe the experiments section can be improved by adding direct comparsion with other long-context models beyond Mamba variants.
I find this is necessary because the core motivation of this work is to address the poor long-context ability of Mambas compared to the transformer-based model, as said in the introduction section. Therefore, it is useful to learn how much LongMamba helps bridge the performance gap. More specifical, the author may follow the [Mamba](https://arxiv.org/abs/2312.00752)'s main experiment setting and compare the LongMamba to varients of transformers (like [Pythia](https://arxiv.org/abs/2304.01373) ) or hypird model

### Questions
(1) How does the LongMamba perform on the code categroy of LongBench?

(2) Does the token filtering process bring extra compute or memory cost?

(3) How does the "local and global channels" behave on larger Mamba model?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces LongMamba, which is a training-free method to enhance Mamba long context performance. It identified that the channels in Mamba have distinct receptive field lengths: local and global. And it hypothesize that this failure of the global channels
to capture global information under extended sequence lengths is the root cause of Mamba’s poor performance in long-context understanding. LongMamba expands the global channels' receptive fields by removing less important tokens.

### Strengths
1. The discovery and explanation of  Mamba models’ limited performance in long contexts are quite interesting.

2. The paper conducts extensive experiments, and LongMamba show its effectiveness

### Weaknesses
1. While I really appreciate the discovery and root analysis of Mamba's limitations regarding long contexts, I find that LongMamba's approach—pruning less important tokens to increase the global channel's receptive field—seems somewhat incremental compared to DeciMamba.

2. LongMamba shows some improvements for long contexts, but it still seems to be somewhat behind transformer-based LLMs designed for long contexts. I understand that the authors are currently using a training-free approach. If training were allowed, would the performance be further enhanced?

3. It would be more convincing if the authors can provide an evaluation on the Ruler benchmark[1].

### Questions
see the weakness section

### Soundness
2

### Presentation
3

### Contribution
2
