# OD-Stega: LLM-Based Near-Imperceptible Steganography via Optimized Distributions

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 3, 5

## Abstract
We consider coverless steganography where a Large Language Model (LLM) drives an arithmetic coding decoder to generate stego-text. An efficient method should embed secret message bits in as few language tokens as possible, while still keeping the stego-text natural and fluent. We show that on the individual token level, this problem is mathematically equivalent to maximizing the entropy of a replacement probability distribution of the next token generation, subject to a constraint on the KL divergence between the chosen probability distribution and the original distribution given by the LLM. A closed-form solution is provided for the optimization problem, which can be computed efficiently. Several important practical issues are also tackled: 1) The combination of the optimized distribution and the vocabulary truncating technique is considered, 2) An often-overlooked tokenization mismatch issue is resolved with a simple prompt selection approach, and 3) The combination of the optimized distribution with other sequence-level selection heuristics to further enhance the efficiency and reliability is studied.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper suggest to distort little bit the probability distribution of LLM in generative steganography to increase the capacity.

### Strengths
* The theory of the paper is decent.
* It is refreshing to see terminology used in steganographic literature.
* I have never thought about issues with tokenization, as I have thought about it about unique. But it is not. This is a big deal jeopardizing a lot of prior art.

### Weaknesses
There are few concerns I have with the work.
* Steganography always thrived to be undetectable. One of the big hallmarks of generative steganography is that if done right, it is actually undetectable. Why would I want to trade off undetectability for a higher capacity? This is very important when one considers square-root law discovered by Andrew Ker [1]. This says that the message embedded by an imperfect steganographic system, which authors have introduced has to decrease faster than square-root of length of the cover, otherwise the system will be detectable. With respect to this, the proposed system have sense only for one-off message where the steganography is not repeated (see works by Andrew Ker on pooled steganalysis [2]). With respect to this, I think that for longer messages and / or repeated communication the improvement in the capacity will be small, otherwise the steganographer will be detectable in the long run. Or the other way around, the method proposed in the paper makes sense when the steganographer sends only one short message. I am not sure this is of practical interest.
* The second flaw of the paper is that it distorts probability of individual tokens. In some sense, the theory therefore assumes IID model and does not take interactions between tokens and the cumulative effects into the consideration. This is not necessarily bad, as one of the big hallmarks of cover-modification steganography was derived under exactly the same conditions, but then it took more than a decade to derive a principled method utilizing this system [4]. But this point should be made clear and explicit. Again, with respect to the above claim.
* My third objection is the evaluation. It seems to me that it makes the Eve (warden, steganalyst) just plain weak. Under Kerckhoffs' principle, she has all the knowledge about the steganographic channel. Why she cannot train a statistical detector, for example by finetuning some LLM, and relies instead on some instructed LLM? This seems just plain wrong to me.
* Discop [5] on page 4 discusses practical issues of arithmetic coding and argues that unless the length of the message is very long, there will be a detectable distortion (see Table II of paper [5]). Your scheme further increases this distortion.

### Questions
I would like to ask authors, if they can comment the weaknesses I have mentioned above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The author presents a novel steganographic method for large language models (LLMs) that integrates probability truncation and optimized distributions.  This approach aims to embed more secret messages while reducing computational complexity and maintaining undetectability.  The paper's primary contribution lies in addressing tokenization errors associated with the use of tokenizers in existing LLMs for steganography.  Extensive experiments are conducted, employing KL divergence and GPT-4 to evaluate the generated text, with results depicted in clear and comprehensible figures.

### Strengths
1. The paper innovatively resolves tokenization errors that occur in existing LLMs used for steganography.
2. The proof for optimizing distribution probabilities is comprehensive and methodologically sound.
3. The graphical representations effectively convey complex information in an accessible manner.

### Weaknesses
1. The flow of arithmetic coding steganography in Figure 1 does not include the message extraction operation for the receiver, which is critical for understanding the full process. Specifically, the figure only shows how the message is embedded using probability intervals, but not how these intervals are used by the receiver to decode the message, making it incomplete.
2. The experimental section lacks an analysis of how different truncation operations impact embedding and extraction times, which are crucial for assessing practical efficiency. The paper mentions truncation, but does not quantify its effect on the computational cost, especially given that truncation affects the precision of probability intervals and thus the number of bits that can be embedded per token.
3. The experiments evaluating GPT-4 only compare different truncation sizes against a baseline, without providing a comparative analysis among these sizes, limiting the understanding of their relative effectiveness. The results show performance differences, but do not offer a clear picture of which truncation size is optimal under different conditions or why.
4. The baseline method used in the experiments is from 2020, and there is no comparison with more recent methods, which may undermine the relevance of the findings. Given the rapid advancements in the field, using a 2020 baseline may not accurately reflect the state-of-the-art performance, and thus, the claimed improvements may not be as significant as suggested.

### Questions
1.T he interval obtained from arithmetic coding mapping 0.10111 should be [0.71875, 0.75). Could you clarify this calculation?
2. Could you include the message extraction operation in the flow of arithmetic coding steganography shown in Figure 1 to provide a complete overview?
3. Please consider adding an analysis of the impact of different truncation operations on embedding and extraction times in the experimental section.
4. In the GPT-4 evaluation experiments, only comparisons against the baseline are provided. Can you include a comparative analysis among the different truncation sizes?
5. It would be useful to add examples and requirements for different secret message lengths relative to B bits, as well as the distinctions between correct and incorrect extractions.
6. The baseline method used is from 2020. Could you provide comparisons with the latest methods to contextualize your contributions?

### Soundness
2

### Presentation
3

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
The paper proposes an LLM-based text steganography method OD-Stega, using an improved adaptive arithmetic coding decoder. The authors considered several practical issues such as tokenization error and computational complexity, and they provided strategies to improve efficiency and reliability.

### Strengths
1. The paper is well-written. The combination of lemma and examples makes the paper easy to read.
2. Consideration of decoding errors is encouraged. 
3. A two-dimensional imperceptibility metric for stegotexts was realized using KL divergence and GPT-4 evaluation.

### Weaknesses
1. The steganographic methods cited and compared in this paper only cover approaches developed before 2020. In recent years, many researchers have proposed perfectly secure steganographic methods based on large language models (LLMs) [1][2][3][4][5]. These methods achieve distribution preservation and make efficient use of the information entropy in the prediction distribution of LLMs, which means that these methods modify the KL divergence to almost 0, while utilization of entropy is close to 1. In my view, the proposed OD-Stega method does not offer any advantage in terms of security, and its embedding rate and runtime efficiency have not been compared with these recent methods. The novelty of this paper is therefore questionable. I suggest the authors add a comparison with these methods, focusing on the trade-off between the proposed method's modification of KL divergence and embedding capacity.

- [1] Zhang, Siyu, et al. "Provably Secure Generative Linguistic Steganography." Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021. 2021.
- [2] Kaptchuk, Gabriel, et al. "Meteor: Cryptographically secure steganography for realistic distributions." Proceedings of the 2021 ACM SIGSAC Conference on Computer and Communications Security. 2021.
- [3] de Witt, Christian Schroeder, et al. "Perfectly secure steganography using minimum entropy coupling." arXiv preprint arXiv:2210.14889 (2022).
- [4] Ding, Jinyang, et al. "Discop: Provably secure steganography in practice based on" distribution copies"." 2023 IEEE Symposium on Security and Privacy (SP). IEEE, 2023.
- [5] Zhang, Xin, et al. "Provably secure public-key steganography based on elliptic curve cryptography." IEEE Transactions on Information Forensics and Security (2024).

2. Lack of steganalysis experiments. The paper uses two metrics, KLD and GPT Evaluation Score, to detect the imperceptibility of stegotext, but it lacks the most direct experiments using steganalysis tools as classifiers between covertexts and stegotexts. Existing linguistic steganalysis tools like [6][7] can only achieve about 50% accuracy when detecting the above provably secure methods [1][2][3][4][5], which is similar to random guessing. Whether the method proposed in the paper can achieve similar safety performance is an important metric.

- [6] Yang, Zhongliang, Yongfeng Huang, and Yu-Jin Zhang. "A fast and efficient text steganalysis method." IEEE Signal Processing Letters 26.4 (2019): 627-631.
- [7] Niu, Yan, et al. "A hybrid R-BILSTM-C neural network based text steganalysis." IEEE Signal Processing Letters 26.12 (2019): 1907-1911.

### Questions
1. The paper refers to the proposed LLM-sampling-based linguistic steganography as coverless steganography. Why is the text generated by normal sampling of LLM not considered by the authors to be cover text?
2. Does the receiver need to know the length of B during decoding? On average, how many repetitions are required for each generation by the sender?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose a new form of LLM-based steganography algorithm, with the added goal that the size of the stego-text should be as small as possible. To achieve that, the authors modify the token probability distribution to increase the entropy of the possible choices, therefore increasing the amount of message that can be secretly embedded. However, to maintain security, this must be done while keeping the new distribution relatively similar to the original one to avoid distinguishing attacks. These two contradicting objectives are modeled into a convex optimization problem. 

The authors provide a small study of so-called tokenization error issue (present already in state-of-the-art). In addition, to avoid computational complexity to explode in some cases, they leverage a simple and existing truncation strategy of the vocabulary. Finally, they adaptatively control the divergence threshold to avoid special situations where very unusual tokens might be selected. 

Experiments have been conducted on LLAMA2-7B with various starting prompts. Examples of stego-test with different parameters values are exhibited.

### Strengths
- the general idea to change the token probability distribution is interesting and it is reasonable to think that it should lead to more compact stego-text. 

- the paper improves over the truncation-based method

### Weaknesses
 - I am not really convinced by the evaluation metric for the security part. You check 1) KL divergence and 2) if GPT4 believes the stego-text was written by a human. The first one is quantitative and we can't relate its value to actual security in practice. The second one is very subjective and might completely miss obvious distinguishing patterns. I understand that maximizing these metrics goes towards higher security, but one has no idea if the final generated stego-text could be detected with advanced statistical attacks. Maybe take as example constructions with some provably security https://eprint.iacr.org/2021/686.pdf (CCS 2021)

- Maybe some argumentation is lacking to explain in what practical cases is LLM-based steganography needed ?

### Questions
-  looking at figure 4, it would have been great to represent which of these points actually lead to incoherent texts (as shown in figure 6 and 7) 

- It would make sense to keep black color for "truncation method" in all your figures, it would be clearer for the reader.

### Soundness
2

### Presentation
3

### Contribution
2
