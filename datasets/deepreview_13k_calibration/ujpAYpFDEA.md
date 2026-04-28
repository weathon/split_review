# Can Watermarked LLMs be Identified by Users via Crafted Prompts?

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 6, 8

## Abstract
Text watermarking for Large Language Models (LLMs) has made significant progress in detecting LLM outputs and preventing misuse. Current watermarking techniques offer high detectability, minimal impact on text quality, and robustness to text editing. 
    However, current researches lack investigation into the imperceptibility of watermarking techniques in LLM services.
    This is crucial as LLM providers may not want to disclose the presence of watermarks in real-world scenarios, as it could reduce user willingness to use the service and make watermarks more vulnerable to attacks. This work is the first to investigate the imperceptibility of watermarked LLMs. We design an identification algorithm called \texttt{Water-Probe} that detects watermarks through well-designed prompts to the LLM. Our key motivation is that current watermarked LLMs expose consistent biases under the same watermark key, resulting in similar differences across prompts under different watermark keys. Experiments show that almost all mainstream watermarking algorithms are easily identified with our well-designed prompts, 
    while \texttt{Water-Probe} demonstrates a minimal false positive rate for non-watermarked LLMs. 
    Finally, we propose that the key to enhancing the imperceptibility of watermarked LLMs is to increase the randomness of watermark key selection. Based on this, we introduce the \texttt{Water-Bag} strategy, which significantly improves watermark imperceptibility by merging multiple watermark keys.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Considering that “even if individual watermarked texts are imperceptible, the distribution of numerous watermarked texts may reveal whether the LLM is watermarked, especially when repeatedly sampling with the same watermark key”, this paper proposed Water-Probe to detect if an LLM service contains watermarks through well-designed prompts then introduced Water-Bag strategy to improve watermark imperceptibility by merging multiple watermark keys.

### Strengths
1 This work is the first study on the imperceptibility of watermarked LLMs. 
2 This paper is well organized and written, make it easy to follow.
3 The experiments are conducted across different LLMs and with different sampling methods and temperature settings. The conclusion and discussion based on the evaluation results are clear.

### Weaknesses
The threat model should be further described, especially in terms of the prior knowledge  assumptions of the detector.

### Questions
How about the blackbox detection on LLMs in real world? What is the difficulty?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposed a method called Water-Probe to detect whether a LLM is watermarked through well-designed prompts. Experiments show the method is effective to almost all mainstream watermarking algorithms. The authors also proposed a strategy to improves watermark imperceptibility by multiple keys.

### Strengths
1. It is reasonable to use repeated sampling to detect whether an LLM has been watermarked. 
2. Prompts have been designed to reveal the connection between generated text and watermark keys in a black-box setting.
3. The evaluation is comprehensive, and many different watermarking methods have been tested. Experimental results also show that the proposed method works.

### Weaknesses
1. Symbol reuse. In Section 3 and Section 4, the symbol $P$ represents both the model distribution in $P_M$ and the prompt in $P_1, P_2, ..., P_N$, which can be confusing. Too many $P$ across line 222 to line 227.
2. Line 289, Figure 2. ‘KTH’ does not refer to anything else in other contexts. Is it Exp-Edit or ITS-Edit?
3. In the method for enhancing the key pseudorandomness of the Water-Bag Strategy, your use of the "set of master keys and their inversions" approach lacks theoretical support. Does "inversions" refer to bit flips, or does it refer to certain keys that satisfy the constraints of equation (12)? If it’s the former, then the claim of enhanced pseudorandomness has no basis; if it’s the latter, the paper does not explain how to derive the inversion key space that satisfies equation (12), and it seems that satisfying (12) does not have a direct relationship with the pseudorandomness of $K^*_j$. The experiments in Table 2 test methods against the attacks proposed by the authors, without directly testing the pseudorandomness of the sequences in the key space using suites like NIST SP 800-22. Ultimately, this seems to only indicate that the specific method enhances defense capabilities against the proposed attacks, rather than demonstrating that the enhancement of pseudorandomness leads to improved defense capabilities, which is inconsistent with the authors' previous claims.

### Questions
1. In Table 1, why Water-Probe-V2 has low detection confidence for KGW series watermarks?
2. Could you provide some experiments on watermark detection on closed-source models such as ChatGPT using your tool? Since the proposed method is a black-box setting, this should be achievable.
3. In the method for enhancing the key pseudorandomness of the Water-Bag Strategy, your use of the "set of master keys and their inversions" approach lacks theoretical support. Does "inversions" refer to bit flips, or does it refer to certain keys that satisfy the constraints of equation (12)? If it’s the former, then the claim of enhanced pseudorandomness has no basis; if it’s the latter, the paper does not explain how to derive the inversion key space that satisfies equation (12), and it seems that satisfying (12) does not have a direct relationship with the pseudorandomness of $K^*_j$. The experiments in Table 2 test methods against the attacks proposed by the authors, without directly testing the pseudorandomness of the sequences in the key space using suites like NIST SP 800-22. Ultimately, this seems to only indicate that the specific method enhances defense capabilities against the proposed attacks, rather than demonstrating that the enhancement of pseudorandomness leads to improved defense capabilities, which is inconsistent with the authors' previous claims.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the imperceptibility of watermarking techniques used in Large Language Models (LLMs). It highlights that while existing watermarking techniques are effective in terms of detectability, minimal impact on text quality, and robustness to editing, they have not been thoroughly examined for their imperceptibility to users. The authors introduce an identification algorithm, Water-Probe, which is capable of detecting watermarks through carefully designed prompts. To enhance watermark imperceptibility, the authors propose a Water-Bag strategy, which merges multiple watermark keys to increase randomness.

### Strengths
- **Accuracy and Robustness**: The experimental results demonstrate the high accuracy and robustness of the Water-Probe algorithm across various LLMs, watermarking methods, and generation settings. The low false positive rate for non-watermarked LLMs further strengthens the algorithm’s reliability.
- **Practical Solution**: The proposed Water-Bag strategy offers a practical solution to improve the imperceptibility of watermarks, which is a critical concern for LLM providers.

### Weaknesses
- **Concept Confusion**: The manuscript mislead concept of watermarking and fingerprinting, the proposed method should be categorized into fingerprinting instead of watermarking. see Question 1.
- **Lack of Controbution**: The authors inputs prompts to see the response of watermarked LLM and non-watermarked LLM, which is so called identification algorithm. The manuscript just defeines some concept, samples prompt to see similarity of the inspected models. 
- **Limited Scope of Water-Probe**: The Water-Probe algorithm might be limited in its application to only certain types of watermarking schemes. The paper does not sufficiently explore how the algorithm would perform against a wider range of watermarking techniques, especially those that are more sophisticated or less predictable.

### Questions
- **Concept Confusion**: the authors mislead watermarking concept.
LLM Watermarking is the process of injecting a invisible identifier into LLM, track unauthorized distribution, or indicate authenticity, withch contains two steps **injection** and **detection**. The author just talk about how to identify LLM output consistency, I never see any discussion about watermark injection in paper. The authors should clarify how their work relates to the injection and detection steps they have outlined, or explain why their approach focuses solely on identification without addressing injection.

- **Unknown Key Sampling Strategy**: the author propose the watermark identification method using setected prompts.
Step 1-3 only discuss the object of identification key sampling, never talk about the detail of identification key sampling.

- **Method Designed**: The author says “Research on the imperceptibility of watermarked LLMs should investigate whether watermarked and non-watermarked LLMs can be distinguished.”. However, in this paper, I never see the sampled prompts and identification method can solve this problem. The authors should clearly illustrate how the proposed method differentiates between watermarked and non-watermarked LLMs. I recommend including a specific experiment or analysis that directly addresses this assertion.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes an identification algorithm to detect watermarks through well-designed prompts to LLMs, as current watermarked LLMs have consistent biases under the same watermark key.

### Strengths
The paper identifies watermarks in a black-box setting. Also, it proposes an effective method to improve watermark imperceptibility.

### Weaknesses
The primary concern I have with the paper is the similarity of distribution differences between prompts in the no-watermark case. First, cosine similarity measures the similarity between two non-zero vectors; thus, the equation Sim(0, 0) in the proof in Appendix B is confusing. Second, if we examine the distances of the elements directly rather than using the Sim function, the distances of the elements in the no-watermark case are approximately zero, suggesting high similarity.

The selection of prompts appears empirical. The paper could be strengthened by providing guidance on generating prompts that produce similar output distributions.

### Questions
Why is the similarity of distribution differences between prompts in the no-watermark case low?

### Soundness
3

### Presentation
3

### Contribution
3
