# Trace Reconstruction for DNA Data Storage using Language Models

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 8, 3, 5

## Abstract
DNA is a promising storage medium due to its high information density and
longevity. However, the storage process introduces errors, thus algorithms and
codes are required for reliable storage. A common important step in the recovery
of the information from DNA is trace reconstruction. In the trace reconstruction
problem, the goal is to construct a sequence from noisy copies corrupted by deletion,
insertion, and substitution errors. In this paper, we propose to use language
models trained with next-token prediction for trace reconstruction. A simple channel
model for the DNA data storage pipeline allows for self-supervised pretraining
on large amounts of synthetic data. Additional finetuning on real data enables us
to adapt to technology-dependent error statistics. The proposed method (TReconLM) outperforms
state-of-the-art trace reconstruction algorithms for DNA data storage, often
recovering significantly more sequences.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors propose a new LLM-based method for the trace reconstruction problem. The problem is reconstruct an unknown string given N noisy copies of the string. These noisy copies ("reads") are a natural byproduct of DNA sequencing technologies. They contain insertion, deletion, and substitution errors. To date, there is no know algorithm to solve this problem theoretically or empirically. For real systems, people use either combinatorial or network based algorithms to output the unknown string from a collection of 2 to 10 noisy reads. The authors compare their GPT-architecture solution to these other algorithms.

For a success metric, the authors use either perfect reconstruction fraction, or measure the average edit/Hamming distances of the reconstructed strings from the ground truth strings. They compare two versions of the GPT-based model: (1) pre-trained on purely synthetic data, (2) fine-tuned on real data. The difference in (2) is that real data may follow a different error pattern, as opposed to synthetic data in (1) which has uniformly distributed errors.

Compared to other methods, the authors show improved performance. In the appendix, they also compare a few other versions, including models with fewer parameters.

### Strengths
The authors provide a new method that gives good results for trace reconstruction, for both real and synthetic datasets.

The authors justify that fine-tuning is both necessary and sufficient to adapt to real data error distributions.

The authors compare against several existing trace reconstruction algorithms, giving a thorough picture of the current ways to solve the problem in practice.

The paper is concise and easy to follow. The plots are clear, with consistent coloring and informative captions.

### Weaknesses
The paper showcases a successful use of LLMs to solve a real problem. But the solution is not particularly surprising, especially as written. Transformers are very powerful, and the trace reconstruction inputs are consistently structured, without a very long context, so the model is clearly going to do pretty well if trained on the exact same data.

I think the biggest open question that is not answered by this paper is: How does the GPT model solve the trace reconstruction problem? Is there a way to analyze the underlying "algorithm" to get some insights into why it does better than the baselines? Are there specific types of instances where GPT does better than ITR consistently? The results between GPT and ITR are pretty close in many of the graphs (e.g., N > 7), so it would be nice to know concretely why / how GPT is outperforming ITR.

I would love to see some more insights that may generalize to other statistical problems. For example, was there anything the authors learned about pre-training or fine-tuning? Are there any lessons about the training algorithm? Or does everything just work "out of the box" with standard implementations of small GPT models? The success of the authors' method may inspire future efforts on using LLMs to solve statistical problems, and therefore, it would be good to share as detailed insights as possible. For example, one open question is what is the minimum model size needs for the trace reconstruction setting in this paper? It seems like 300M is enough, but 3M is too small?

The paper is missing some key technical details about the training process, hyperparameter tuning, training time, number of GPUs, etc. I would like to see this in the final paper for full transparency.

### Questions
1) Another baseline would be how well can GPT Mini / Gemini Flash solve this problem in a few-shot manner? Is there a prompt that can get similar performance without needing to pre-train or fine-tune? This would make it easier to implement via an API rather than needing GPUs and knowing how to train LLMs (e.g, for biologists who want to solve this problem).

2) Can you perform some interpretability of the network to see what algorithm the GPT model is implementing under the hood? And do you think the fine-tuned model is doing something fundamentally different than the pre-trained model?

3) It would be helpful to dig deeper into this topic, and push the limits of what the LLMs are capable of. The point here is not just to try random other settings (this would not be a good use of time). The point is to develop general insights that can guide future researchers that want to know if an LLM can solve their (more complicated) statistical problem. For example, there are many variations of this problem that are easy to try synthetically (or others that the authors think would help undercover ideas that could inform (2) above):
- use very long reads, e.g., O(1000) bases --> do you need a much bigger model for this?
- increasing the read count and the error rate -- what happens if p_UB goes up to 0.4 but there are O(100) reads per cluster?
- for Figure 5, how many reads are necessary to get to ~0.0 error?

4) Overall, I would be happy to increase my score if the authors could show some more general findings beyond just "LLMs can solve trace reconstruction if they have enough data and enough parameters"

Minor comments:
- the logarithmic plot y-axis is a bit hard to read, I would also add into the appendix a table of the results for the average Hamming / Levenshtein distances at each N.
- Typo in Appendix D title "PARAMTERS"

-----------------

Post rebuttal: Increasing score 5 --> 6 since the authors added new parts to the paper, including:
1. attention maps
2. more training details
3. scaling laws
4. large cluster experiments

I encourage the authors to incorporate these more detailed / technical analyses to the main body of the paper, to make it clear that their method took some care to get to work.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a method for trace reconstruction in DNA data storage using language models. The approach involves training on synthetic data, with subsequent finetuning on real datasets to improve performance on technology-specific error distributions. Experimental results show that the proposed method outperforms existing approaches on the Hamming and Levenshtein distance metrics.

### Strengths
- The paper is very well written.
- The approach is innovative.
- The concept is novel to my knowledge.
- The use case (high noise, few traces) is very relevant to real-world scenarios.
- Superior performance compared to the state of the art is demonstrated.

### Weaknesses
Major:
- Although the model can handle different error patterns through fine-tuning, it may struggle with entirely new or highly variable error profiles in unseen data. Specifically, it is unclear how well burst errors would be handled. The fine-tuning approach, while beneficial for adapting to known error distributions, might not generalize well to scenarios where the error characteristics change significantly or exhibit complex dependencies not present in the training data. For instance, if the training data primarily contains single nucleotide errors, the model's performance could degrade substantially when faced with longer insertions or deletions, or correlated errors that span multiple bases. The paper does not provide a rigorous analysis of the model's robustness to such shifts in the error landscape.

Minor:
- Figure 3: The parameter N (number of traces) should be introduced.
- Line 235: Please explain why you are considering decoder-only transformers.

### Questions
- One-hot encoded sequences are padded to a fixed predetermined length. As DNA synthesis methods are being developed that produce significantly longer oligonucleotides, is this fixed-length scheme generally compatible with sequencing technologies that produce long variable-length reads (nanopore)?
- The authors assume that the original sequence consists of bases chosen uniformly at random. If fine-tuning on real data would not be feasible, how would the scheme need to be adapted to accommodate non-uniform distributions?
- It would be nice to see an evaluation of the minimum number of traces required for given I/D/S error probabilities.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The author(s) introduced a DL-based approach for reconstructing DNA sequences from clustered DNA reads obtained through a DNA storage pipeline.  The study utilizes a next-token prediction transformer for this purpose. The model is pre-trained on synthetic data and subsequently fine-tuned using a specific open wet-lab dataset.

### Strengths
Sequence reconstruction is a challenging and valuable topic within the fields of DNA storage and bioinformatics. 

The introduction of a next-token prediction transformer-based method for sequence reconstruction marks a novel contribution to the DNA storage research community. 

The experimental outcomes are promising.

### Weaknesses
The reviewer’s primary concern relates to the limited novelty within the machine learning or learning representation community, as the work appears to be an application of established deep learning techniques. The authors may spend more context to address this comment in their rebuttal if there is one.

The writting was somehow not treated carefully. For example, since the caption of Figure 3, the proposed method is abruptly referred to as “GPT”. Firstly, the proposed method lacks a formal name, and “GPT” is not a good choice. Secondly, even GPT is not predifined in the text.

Line 199. The author(s) assert that they "do not consider this (the discrepancy between the pretraining and finetuning data) here" without providing a rationale. The reviewer thought this may not be acceptable.

As a DL-based method, the absence of comparative experiments with the closely related transformer models, DNAformer and RobuSeqNet, within the main text requires a justifiable explanation.

Why is it necessary to train separate models for (sequence length $N=2$ to $N=5$) and (sequence length $N=6$ to $N=10$)? If this is necessary, the sequence length is a hyperparameter that requires analysis. (In Line 420, the author(s) refer to "sequences of length two to five". The reviewer suspects that this might actually refer to the cardinality of clusters, with the range extending from $N=2$ to $N=5$.)

What is the "subcluster" for in Line 392?

The reviewer posits that no method is capable of effectively reconstructing sequences from clusters with a cardinality of  $N=2$, due to the insufficient information available. However, the finetuned results presented in Figures 6 and 8 for $N=2$ are promising and appear to contradict this assertion. The authors are kindly requested to provide an explanation for this. Could it be that the model learned underlying patterns or distributions specific to the wet-lab data?

### Questions
1. Line 199. The author(s) assert that they "do not consider this (the discrepancy between the pretraining and finetuning data) here" without providing a rationale. The reviewer thought this may not be acceptable. 
1. As a DL-based method, the absence of comparative experiments with the closely related transformer models, DNAformer and RobuSeqNet, within the main text requires a justifiable explanation. 
1. Why is it necessary to train separate models for (sequence length $N=2$ to $N=5$) and (sequence length $N=6$ to $N=10$)? If this is necessary, the sequence length is a hyperparameter that requires analysis. (In Line 420, the author(s) refer to "sequences of length two to five". The reviewer suspects that this might actually refer to the cardinality of clusters, with the range extending from $N=2$ to $N=5$.)
1. What is the "subcluster" for in Line 392?
1. The reviewer posits that no method is capable of effectively reconstructing sequences from clusters with a cardinality of  $N=2$, due to the insufficient information available. However, the finetuned results presented in Figures 6 and 8 for $N=2$ are promising and appear to contradict this assertion. The authors are kindly requested to provide an explanation for this. Could it be that the model learned underlying patterns or distributions specific to the wet-lab data?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores trace reconstruction of DNA sequences using a GPT model. Trace reconstruction aims to recover the original DNA sequence from several corrupted versions containing insertion, deletion, and substitution errors. On synthetic data with a fixed error probability, the GPT model performs well. However, while a pretrained GPT model did not achieve effective results on real data, fine-tuning significantly improved its performance, surpassing previous methods.

### Strengths
Applying GPT to DNA storage problems is a promising direction, especially since tasks like multiple sequence alignment and trace reconstruction typically demand high computational resources. This work suggests the potential of using large language models (LLMs) to streamline these processes.

### Weaknesses
Unlike traditional dynamic programming-based algorithms, the proposed GPT model relies heavily on dataset-specific statistics, as seen in real-world experiments where fine-tuning was necessary. The authors claim that training on a uniform distribution of error probabilities covers most DNA storage systems, but this claim is not sufficiently supported by experimental evidence. The experiments do not demonstrate that the model can generalize to unseen error distributions, which is a critical requirement for real-world applicability. Furthermore, the performance drop for larger cluster sizes in Section 5.3.2 remains a concern. While the authors mention hyperparameter tuning, the lack of specific details on the tuning process and the resulting improvements makes it difficult to assess the robustness of the method. The provided data and code are appreciated, but the core issue of limited generalization remains unaddressed.

### Questions
Please check weaknesses

### Soundness
3

### Presentation
3

### Contribution
3
