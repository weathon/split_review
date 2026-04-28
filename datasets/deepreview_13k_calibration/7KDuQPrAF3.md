# A Foundation Model for Error Correction Codes

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 3, 8

## Abstract
In recent years, Artificial Intelligence has undergone a paradigm shift with the rise of foundation models, which are trained on large amounts of data, typically in a self-supervised way, and can then be adapted to a wide range of downstream tasks. In this work, we propose the first foundation model for Error Correction Codes. This model is trained on multiple codes and can then be applied to an unseen code. To enable this, we extend the Transformer architecture in multiple ways: (1) a code-invariant initial embedding, which is also position- and length-invariant, (2) a learned modulation of the attention maps that is conditioned on the Tanner graph, and (3) a length-invariant code-aware noise prediction module that is based on the parity-check matrix. The proposed architecture is trained on multiple short- and medium-length codes and is able to generalize to unseen codes. Its performance on these codes matches and even outperforms the state of the art, despite having a smaller capacity than the leading code-specific transformers. The suggested framework therefore demonstrates, for the first time, the benefits of learning a universal decoder rather than a neural decoder optimized for a given code.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors proposed a model and is trained on multiple codes and can then be applied to an
unseen code.
Transformer architecture in multipleways: 
(1) a code-invariant initial embedding, which is also position- and lengthinvariant,
(2) a learned modulation of the attention maps that is conditioned on the Tanner graph
(3) a length-invariant code-aware noise prediction module that is based on the parity-check matrix

### Strengths
1.Error control coding implemtation on the deep learning technique is highly encourgaing.
2.Authors got the optimized Results in terms of BER.

### Weaknesses
1.Conclusion should be rewritten based on the results presented mentioning the future scope.

### Questions
1.Conclusion should be rewritten based on the results presented mentioning the future scope.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work embarks on a very ambitious journey towards creating a foundation code for all downstream ECCs. The suggested structure here largely depends on a prior NeurIPS paper ([NeurIPS’22] Choukroun et al., Error Correction Code Transformer, presumably by the same authors) in that it is a specialized Transformer with bitwise embedding and parity-check-matrix-dependent masking, as appropriate for ECC. Albeit similar to prior work, the present proposal contains enough new materials and gives a highly convincing architecture based on code-aware aggregation that depends on the parity-check matrix as well as code-invariant bitwise embedding.

### Strengths
The proposed idea is very ambitious, and is based on a highly innovative specialization of the Transformer to the classical problem of decoding received codewords of linear codes. The proposed ideas/strategies are very interesting and convincing (such as bitwise embedding independent of particular codes and incorporation of the parity check matrix in the embedding function). The impact on the field of digital communication and data storage could be large.

### Weaknesses
The main issue is that the training of the model is done using codes with lengths up to 150 only, hardly a sufficient length to reflect many modern codes of important applications (testing is also done on relatively small codes, with the largest being a 255 bit BCH). The popular LDPC codes are also curiously missing in the training as well as in the performance evaluation. Likewise for meaningfully long Polar codes. In this sense, I am not sure if the term “foundation model” is justified here. In sum, the idea seems very good, but the validation comes short of a reasonable expectation. I do not feel just saying "we have limited computing resources" would be a good enough excuse for such an ambitious title.

Writings on various parts seem direct copies from [NeurIPS’22] Choukroun et al., Error Correction Code Transformer. Try to differentiate.

In Tables 1 and 2, the proposed method seem noticeably worse than ECCT on larger codes. Also, In Table 3, ECCT+DM+II gives the best results. Explanations would be  good.

### Questions
Please respond to the mentioned weaknesses above.

In Tables 1 and 2, the proposed method seem noticeably worse than ECCT on larger codes. Also, In Table 3, ECCT+DM+II gives the best results. Explanations would be  good.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper attempts to develop foundation model for Error Correction Codes that is trained on large data so that it can be used later for any downstream task. Specifically, authors aim to adapt the Transformer input embedding for robustness to code length variations. To learn the code structure, they use the positional embedding, that is integrated into the self-attention via a learned mapping of the node distances in the Tanner graph. Moreover, for code awareness and channel noise prediction, the paper employs a size-invariant prediction module that is conditioned on the parity-check matrix. In simulations, they tested on codes that are unseen during training. They showed that the proposed FECCT method matches or sometimes perform better than the
state of art.

### Strengths
-the paper takes a foundational approach to the decoding problem in error correcting codes, which is intellectually interesting. Clearly being able to decode any type of code is an interesting intriguing  exercise.
- the paper advanced the design of generalist decoders relative to existing generalist decoders by using new embedding and grounding techniques.

### Weaknesses
 -Although the design of foundational decoders are very interesting intellectual exercise, the real world impact of it is close to none if not zero.  The reason is that error correcting codes are designed and deployed once and their training is not a big deal even if someone takes deep neural network decoders as opposed to classical BP methods. But more importantly, there is another argument against the value of these generalist decoders: The important thing to recall is that capacity achieving codes exists for long codes and their BP decoders are close to ML performance, I.e., optimal decoders. So there is no gain of these deep neural decoders in long codes. The focus should be short codes for which we do not have good BP decoders. However, for short codes, we really do not need foundational decoders as one can design and easily train specialized neural decoders for the short codes that will very likely beat the performance of generalist decoders for all lengths. It is clear to believe that a generalist decoder will not be able to perform a specialized deep neural decoder for short lengths, unless the authors can show their generalist decoder can beat the performance of state of art short length (less that 200 bits) code decoders, specialized for that specific code length.

-what is the performance in the tables? I see that 3 different values of Eb/N0 is used as the channel input signal (bit) power to noise ratio but What about reported numbers as performance. What are they? I like to see how these reported numbers translate to the error rate performance, as it is the only thing that matters in communication. It does not look like that the authors picked a particular error rate and report the corresponding Required Eb/N0 to achieve such an error rate. Because in that case the lower number is associated with the better scheme not the higher (as the authors stated in the paper). The presentation of the performance results is not aligned with standard practices in the coding community, making it difficult to assess the practical implications of the proposed method. It's crucial to report performance in terms of bit error rate (BER) or frame error rate (FER) versus Eb/N0, which allows for a direct comparison with existing coding schemes.

-the authors need to compare their scheme with Choukroun & Wolf (2022b) which is shown to be superior to ECCT. The lack of comparison against this more recent and higher-performing method significantly weakens the claims of the paper. The authors should have benchmarked their approach against the state-of-the-art in neural decoding, which includes methods beyond the original ECCT.

### Questions
please compare the proposed generalist decoder at short lengths (less than 200 bits) with that of specialized decoders at those lengths. Because as I pointed out this is where these foundational decoders would show value if any.

-please plot error rate plots rather than the reporting used in the paper which is not insightful.

-it would be helpful to compare your proposed work with that of
Choukroun & Wolf (2022b) which extends and enhances ECCT via Denoising diffusion in error correction codes and have far superior performance than ECCT.

-the paper novelty is arguable in light of ECCT design architecture. For the most part following similar development as ECCT. Can the authors elaborate on the novelty relative to ECCT.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper builds on top of Error Correction Code Transformer(ECCT), made a few structural change to build a "foundational" ECCT (FECCT) model for block code decoding. 

FECCT is a generalized version of ECCT:

(1) FECCT is not length-dependent, H-dependent, and not even code-dependent, thus can be trained once can be used for wide range of block codes, with good performance (matching/beating ECCT mostly, and beat BP by a large margin.). Some finetuning can even lead to better performance.

(2) FECCT could an important milestone of deploying neural decoders to real world given its potential, still a lot of hard work is required till that day.

### Strengths
(1) Overall, FECCT is very plausible method, since FECCT is more like an "decoding algorithm" rather than simply "neural decoder". My definition of "decoding algorithm" means the input is H matrix  and received codeword  (just like BP algorithm), and the output should be decoded message. While other neural decoder has dependency on code/length/H/etc. As of my understanding, FECCT has learned some interesting advanced BP-like algorithm, that can be beneficial for a wide family of block codes.

(2) FECCT is built on top of ECCT, the generalization performance on non-zero codewords are preserved, which makes training feasible. FECCT's H-dependent attention is a generalized version of ECCT's attention, which lead to better decoding capability. The proposed neural structure makes sense, and lead to good generalization performance.

(3) The experiment on unseen code with different code family and block length are interesting, which make (1)'s claim stronger that FECCT is more of an "decoding algorithm".

Overall, this becomes an interesting work, at least for neural decoder research, first time shows that a "decoding algorithm" rather than a complicated mapping can be learned.

### Weaknesses
1. The experiments are mostly built on short block codes (<128, test unseen for 255 at most), while typical capacity-approaching codes such as QC-LDPC has much longer block length. Performance on long block length is going to make this paper stronger, due to long block code's capacity-approaching performance. Specifically, the lack of evaluation on codes with lengths in the thousands or tens of thousands is a significant gap. The performance of FECCT on short codes is promising, but it remains unclear if the observed gains will translate to longer, more practical codes. The paper should include results on codes with lengths more relevant to real-world applications, such as those used in modern communication standards.

2. Interpretability: FECCT should have been learned some interesting algorithm, that can be interpreted as an advanced version of BP. We do see some part of interpretations in the appendix, but not solid enough to get insight on what FECCT's algorithm means. The provided visualizations of attention matrices are a good starting point, but they don't provide a clear understanding of the underlying decoding process. A more detailed analysis is needed to understand how FECCT is leveraging the parity check matrix and received codeword to perform decoding. For example, it would be beneficial to analyze how the attention weights change over different iterations and for different types of errors. A more in-depth analysis of the learned algorithm is needed to truly understand the inner workings of FECCT.

3. Complexity of network: attention-based neural network are very complex. Deploying the FEECT to any real world production requires some hard work on complexity reduction. In its current form, I am not seeing FECCT can be deployed to modem in short time.  Note that channel coding are heavily used in all modern wireless communication systems, which requires minimal latency, high throughput, and low cost. The computational cost of the attention mechanism, especially for larger codes, could be a major bottleneck. The paper should include a more detailed analysis of the computational complexity of FECCT, including the number of parameters and the required FLOPs. Furthermore, the authors should discuss potential techniques for reducing the complexity of the network, such as pruning or quantization, and provide some preliminary results on the impact of these techniques on performance.

### Questions
N/A

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
