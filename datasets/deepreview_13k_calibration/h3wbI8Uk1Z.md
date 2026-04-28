# RNNs are not Transformers (Yet):  The Key Bottleneck on In-Context Retrieval

- Decision: Accept
- Avg Score: 5.50
- Scores: 3, 6, 8, 5

## Abstract
This paper investigates the gap in representation powers of Recurrent Neural Networks (RNNs) and Transformers in the context of solving algorithmic problems. We focus on understanding whether RNNs, known for their memory efficiency in handling long sequences, can match the performance of Transformers, particularly when enhanced with Chain-of-Thought (CoT) prompting. Our theoretical analysis reveals that CoT improves RNNs but is insufficient to close the gap with Transformers. A key bottleneck lies in the inability of RNNs to perfectly retrieve information from the context, even with CoT: 
for several tasks that explicitly or implicitly require this capability, such as associative recall and determining if a graph is a tree, we prove that RNNs are not expressive enough to solve the tasks while Transformers can solve them with ease.
Conversely, we prove that adopting techniques to enhance the in-context retrieval capability of RNNs, including Retrieval-Augmented Generation (RAG) and adding a single Transformer layer, can elevate RNNs to be capable of solving all polynomial-time solvable problems with CoT, hence closing the representation gap with Transformers

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates the representational capabilities of RNNs and Transformers, both with and without Chain-of-Thought (CoT). Assuming a limited RNN state size of O(log n), the authors show that RNNs augmented with CoT have greater representational power than standard RNNs, but are still less powerful than Transformers with CoT. To bridge this gap, the authors propose adding in-context retrieval mechanisms to RNNs, showing that this extension enables RNNs with CoT to solve polynomial-time problems, effectively matching the capabilities of Transformers with CoT.


Informally, the relationships can be summarized as:
- Standard RNN < RNN + CoT < Transformer + CoT
- RNN + In-Context Retrieval + CoT ~= Transformer + CoT

### Strengths
- The paper is well-structured and clearly written, main ideas and results are easy to follow.
    
- The paper constructs building blocks for Transformers that can be used to solve various tasks, including indexing, associative recall, c-gram retrieval, and counting. It provides detailed analyses of how these problems can be addressed using different architectures and shows their limitations.
    
- The authors support their theoretical results with empirical evaluations on tasks such as IsTree and HotPotQA, thus strengthening their claims.
    
- Show that in-context retrieval, similar to attention mechanism, is sufficient to close the gap between RNNs and Transformers with CoT, and suggest how to build more expressive RNN architectures.

### Weaknesses
1. The authors compare RNNs and Transformers under different assumptions regarding their state sizes. Specifically, they limit RNNs to a limited hidden state size of O(log n), while allowing Transformers to have an effective state size that grows linearly with the input length due to the accumulation of key-value pairs in self-attention. A decoder-only Transformer can be viewed as an RNN with a recurrent state that increases linearly -- adding each processed input to the key-value cache:  in transformer h_t = Transformer(x_t, [h_1, …, h_{t-1}]), in RNN h_{t}  = RNN(x_t, h_{t-1}); In other words, the results obtained are equivalent to comparing RNNs with limited state sizes to RNNs with linearly growing state sizes. There is nothing inherently specific to Transformers in this comparison. The key differentiator in this comparison is the state size rather than any unique property of Transformers. Therefore, concluding that models with larger state sizes have more expressive power than those with limited state sizes is unsurprising.
    
2. Violation of initial assumptions with in-context retrieval. By introducing in-context retrieval to RNNs, the model effectively needs to store the entire input sequence, resulting in O(n) state size requirements - similar to Transformers. This breaks the initial assumption of a limited-size RNN state O(log n) used to state RNNs limitations. As a result, the proposed solution does not address the original problem under the same constraints.
    
3. The proposed solution of adding in-context retrieval to RNNs essentially increases the state size linearly, effectively transforming the RNN into an RNN with linearly growing state size, which resembles a decoder-only Transformer. This leads to the somewhat tautological conclusion that to close the gap between RNNs and Transformers, one should make a Transformer-like model out of an RNN.
    
4. Overlap with existing concepts is not discussed. The relationship between RNNs with CoT and Adaptive Computation Time (ACT) mechanisms is not fully explored. Since CoT can be seen as a form of ACT, and RNNs with ACT have been previously studied, the novelty of the findings may be limited. A deeper exploration of how this work builds upon or differs from existing research on RNNs with ACT could strengthen the contribution.

### Questions
Please address points from weaknesses as questions if authors do not agree.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the representational limitations of Recurrent Neural Networks (RNNs) compared to Transformers in handling sequence modeling tasks. It particularly examines RNNs’ in-context retrieval capabilities, which are essential for tasks requiring memory and context comprehension. Through theoretical analysis and empirical validation, the authors identify the inherent weaknesses of RNNs in retrieving information across long sequences and propose potential methods to bridge the performance gap between RNNs and Transformers.

### Strengths
Originality:
The paper tackles a unique question—whether RNNs can be enhanced to achieve Transformer-like in-context retrieval. By applying communication complexity and information-theoretic methods, it provides a fresh perspective on RNN limitations. Proposing hybrid architectures and Retrieval-Augmented Generation (RAG) is an innovative approach to bridging this gap.

Quality:
The paper is theoretically rigorous, with strong proofs demonstrating RNN limitations. The authors conduct well-designed empirical experiments that validate the theoretical claims on both synthetic and real-world tasks, making the results robust and credible.

Clarity:
The structure is logical, with clear definitions and effective visuals that aid understanding. Complex proofs could benefit from simplified explanations, but overall, the writing is accessible and well-organized.

Significance:
This work addresses a critical issue in model efficiency, with practical implications for memory-constrained applications. It lays a solid theoretical foundation for future research on enhancing RNNs, potentially impacting both low-resource applications and the development of hybrid model architectures.

### Weaknesses
1.This paper spends a large section explaining the well-known concepts in AI community like Language Models and CoT while ignoring the explanation of communication complexity and other less-known concepts that are also important in the proof. It would be better to shift the focus of concept explanation. 

2. In some cases, with enough training, RNN may have the ability to better organize information based on the original O(n) bit. For example, based on the case of in-context retrieval, it may be possible to finetune the RNN to enable it to achieve the information retrieval process with the deepening of layers. e.g. the hidden states in shallow layers store the raw information and the deeper layers add organized information (like the regular expression for retrieval ) into the hidden state.  Please disprove this possibility.

### Questions
Why in-context retrieval can not be deemed as a part of COT?
Since I tried RWKV6 -7B and it can retrieve in context words without the help of regular express function but with the help of CoT. 
I tried api on https://huggingface.co/spaces/BlinkDL/RWKV-Gradio-2
My input is: 

Assistant: ”How can we craft an engaging story featuring vampires on Mars? Let's think step by step and provide an expert response. “ What's the word between 'featuring' and 'on'. Think step by step.

The result is unstable but primarily consist of 'vampire' and 'mars‘， which means RWKV has somewhat retrieval ability.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper compares the performance differences between RNNs and Transformers when enhanced with chain of thought (CoT) reasoning. The term RNN is used in a broad sense to refer to the class of architectures that are linear time and constant memory with respect to sequence length. This paper demonstrates, both theoretically and empirically, that while CoT enhances the performance of RNNs, it is not sufficient to close the gap between RNNs and Transformers. To close this gap, the authors demonstrate that retrieval-augmented generation or adding a single transformer layer is sufficient.

### Strengths
1. This is a well-designed study with a focused question, along with theoretical and empirical support for its conclusions.
2. This paper’s theoretical analysis is a strong contribution, given the numerous prior works that empirically find hybridization and RAG help close the performance gap between transformers and RNNs.

### Weaknesses
1. Perhaps this is a misunderstanding, but line 297 seems to contradict Arora et al. (2023), who observe that while transformers outperform RNNs on associative recall, certain RNNs can perform associative recall. Claiming that “constant-size RNNs cannot solve any of the four tasks” seems too strong, given that Theorem 4.6 is only true for “large enough $n$.” This paper would benefit from the addition of a paragraph reconciling this claim with the empirical results of prior work.
2. The use of IsTree as a synthetic task could be better motivated. As currently written, it seems that this task was chosen simply because it does not obviously require retrieval to solve which is not unique to IsTree. It would be helpful to expand on the authors' rationale.

### Questions
1. Why were the word embedding and decoding heads frozen in the experiments for Figures 2 and 4?
2. How do the author's define a "RNN with o(n)-bit memory"?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates the gap in representation power between Transformers and Recurrent Neural Networks (RNNs) and examines whether RNNs, with techniques like Chain-of-Thought (CoT) prompting, can achieve comparable performance. Through theoretical analysis, the authors demonstrate that RNNs lack the expressiveness needed to handle in-context retrieval tasks, such as associative recall and graph recognition, that Transformers handle with ease. They further support these findings with empirical evidence from both synthetic tasks and natural language experiments, showing that while CoT prompting improves RNNs, it alone is insufficient to bridge the gap.
The authors propose that enhancing RNNs with Retrieval-Augmented Generation (RAG) or adding a Transformer layer can significantly close this performance gap, bringing RNNs closer to Transformer-level capabilities. However, they also acknowledge that practical challenges, such as computational costs and scalability, may arise when implementing these improvements, suggesting a trade-off between efficiency and retrieval effectiveness.

### Strengths
A key strength of this paper is its use of theoretical lower bounds to rigorously show that RNNs lack the expressiveness needed for certain in-context retrieval tasks, unlike Transformers. This analytical approach confirms that RNN limitations are inherent, not merely practical, underscoring the need for hybrid architectures or additional layers to bridge the performance gap. Additionally, the paper validates these findings through empirical experiments across various tasks (such as associative recall and graph recognition), demonstrating that the theoretical limitations are evident in real applications as well.
The authors also provide practical techniques—like Retrieval-Augmented Generation (RAG) and hybrid architectures involving Transformer layers—that make their findings actionable and relevant for architecture design in large language models (LLMs). By identifying specific ways to improve RNNs, the paper offers a path toward resource-efficient alternatives to Transformers, valuable for applications in memory-constrained or mobile environments. Moreover, their analysis sheds light on the mechanisms behind in-context learning, clarifying what capabilities make Transformers excel and highlighting specific limitations in RNNs. This deeper understanding could inform future research on in-context retrieval and neural network architecture design.

### Weaknesses
Readability and Structure: The paper is hard to follow due to poor language flow, making the argument difficult to track.
Redundant content, especially on Chain of Thought (CoT) prompting, appears in both the Related Work and Preliminaries sections. Consolidating these would improve readability. Some definitions are introduced but not utilized in the main text, adding unnecessary complexity.

Depth of Discussion and Empirical Validation: The paper discusses two main ideas: first, that Chain of Thought (CoT) prompting can improve RNNs but is insufficient to fully bridge the representation gap with Transformers; and second, that enhancing the in-context retrieval capability of RNNs can potentially close this gap. However, each of these points would benefit from deeper discussion and more practical experiments. The empirical validation is insufficient; model comparisons are not “apple-to-apple, limiting the clarity and robustness of results.

### Questions
None

### Soundness
3

### Presentation
2

### Contribution
3
