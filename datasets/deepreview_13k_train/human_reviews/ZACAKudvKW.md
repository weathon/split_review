# Watermarking for User Identification in Large Language Models

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
We identify a new task for watermarking -- namely the simultaneous identification of text as being automatically generated alongside the identification of the LLM user. 
We show that a naïve approach that treats a text as artificially generated if a user is correctly identified is prone to problems of false positives arising from multiple hypothesis comparison. 
We propose a novel approach (Our code is submitted with the supplementary material. We will also open it on Github after the anonymity period.) that retains almost similar rates as the number of users increase. We derive theoretical bounds that support our experimental approach.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes a method for achieving both output watermarking and user identification for LLMs.

### Strengths
- LLM watermarking is an important topic for the research community.
- The inclusion of a theoretical analysis strengthens the paper.

### Weaknesses
 - Although the proposed method improves on baseline FPR values, the overall FPR (>0.01) is still too high for practical applications.
- Watermarks can significantly impact text quality, but the paper lacks any analysis of this issue.
- Paraphrasing, whether done once or multiple times, may weaken the watermark because of the hash's sensitivity to small changes.

Minor Points
- The citations need to be adjusted. The authors should use \citep for most citations, except where the citation is the subject or object of the sentence.
- Some tables and figures would benefit from more descriptive captions. For example, Figures 2–7 and Tables 2–5 lack clear descriptions.

### Questions
Given a fixed prompt, does the watermark affect output diversity?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores a new problem for LLM watermarking with a specific focus on user identification. The authors address the challenge of false recognition, where non-watermarked text may be mistakenly classified as watermarked, especially as the user count increases. To tackle this, the paper introduces a Dual Watermark Inspector (DWI) and a Hybrid Dual Watermark Inspector (HDWI) approach, aiming to improve the robustness of watermark detection by reducing false positives. The paper offers a combination of theoretical derivations and empirical validations, suggesting that DWI and HDWI outperform existing watermarking methods in accuracy and false positive control.

### Strengths
1. Addresses a pressing issue of false positives in multi-user watermarking, which is important for the practical use of watermarking in AI applications.

2. Introduces a new dual watermarking approach that embeds user identity while preserving the text's integrity, showing significant improvement in error rates.

### Weaknesses
1. The presentation lacks clarity in explaining the watermarking process. I suggest that the authors include a detailed algorithmic outline to demonstrate how watermark generation and detection are performed. It is currently unclear how the integer key (user ID) is embedded into the generated text. Additionally, based on my understanding, this method is an extension involving when to add Gumbel noise for embedding the watermark, with the primary approach building on existing methods.

2. The citation formatting (using \citep and \citet) should be corrected. Furthermore, the term "Stochastic sampling" in lines 151-152 needs clarification—what exactly is meant by this here? Regarding the hash function, you currently rely on the previous two tokens for hashing. However, as Aaronson suggests, a small window size can compromise pseudorandomness. It would be beneficial to either use a larger window size or store a two-gram history to prevent repetition issues. The use of a small window size for hashing also means that with the same two-gram prefix, the randomness becomes fixed, which may lead to frequent repetitions or reduced detectability.

3. From my understanding, user identification could naturally be addressed through multi-bit watermarking techniques. The statement in lines 104-106, "no methods have explored the task of retrieving information from watermarked text intermingled with unwatermarked text," is unclear. I recommend expanding on this point and providing a more detailed discussion of multi-bit watermarking, especially in relation to user identification.

### Questions
How do DWI and HDWI methods perform computationally when applied to LLMs with larger user bases?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a new watermark encoding approach that divides the tasks of identifying whether text is generated by a large language model (LLM) and determining which user generated it. By separately encoding these two types of information, the proposed method alleviates the issue faced by traditional Full Key Encoding (FKE) methods, which experience increased false positive rates (FPR) as the number of users grows.

### Strengths
1. Identified a Significant Problem: The issue addressed in this paper is highly relevant and important, particularly in the context of managing LLM-generated content.
2. Effective Experimental Results: The experiments convincingly demonstrate that the proposed method effectively mitigates the false positive rate (FPR), particularly as the user count increases.

### Weaknesses
1. Insufficient Comparison with Existing Methods: While the authors constructed some baselines for comparison, the analysis against existing FKE methods is not comprehensive. Notably, the paper does not mention other multi-bit watermarking techniques that can extract user identity, such as MPAC[1] and Codable Watermark[2].
2. Limited Experimental Scope: The main experiments rely on only one model and one dataset, which raises concerns about the generalizability of the findings. A broader range of models and datasets would strengthen the claims made.
3. Lack of Scientific Rigor in Writing: The overall writing lacks scientific rigor, with unclear logic and weak structural organization. Improved clarity and coherence would enhance the readability and impact of the paper.

### Questions
See the weaknesses section.

### Soundness
2

### Presentation
1

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
This paper addresses the false recognition problem in watermarking large language models (LLMs), specifically focusing on simultaneous detection of machine-generated text and user identification. The authors propose a novel Dual Watermark Inspector (DWI) method that separately encodes indicator and key information into generated text. They provide theoretical bounds for false positive rates and demonstrate empirically that their method significantly reduces false positives compared to baseline approaches. The paper includes extensive experiments validating the method's effectiveness across different settings and robustness against insertion/deletion attacks.

### Strengths
- Practical relevance for real-world LLM deployment and governance
- Comprehensive empirical evaluation across various settings (watermark ratios, key capacities, sample sizes)

### Weaknesses
While the paper presents a sound approach, it has several limitations in both technical depth and presentation clarity that could be improved upon.

1. Limited comparison with other recent watermarking methods beyond the baseline FKE approach. The paper primarily focuses on comparing with one baseline method, missing opportunities to demonstrate advantages over other state-of-the-art approaches.

2. The trade-off between accuracy and false positive rate could be analyzed more thoroughly. While the paper shows improvements in false positive rates, it lacks detailed analysis of how this affects other performance metrics across different scenarios.

3. The choice of ratio r between indicator and key information tokens appears somewhat arbitrary. The paper does not provide sufficient theoretical or empirical justification for the selected ratio values.

4. Impact on text quality and fluency not thoroughly discussed or evaluated. The paper focuses on detection metrics but lacks analysis of how the watermarking method affects the generated text's quality and naturalness.

5. Computational overhead of the proposed method compared to baseline not clearly addressed. The additional complexity introduced by the dual watermarking approach is not quantified or discussed in terms of practical implementation costs.

6. Writing and presentation issues detract from the paper's clarity. Several technical terms are used before being properly defined, figure captions lack detail, and important implementation details are scattered between the main text and appendix. The mathematical notation also shows some inconsistency across sections.

### Questions
- How does the method perform with very short text sequences?
- Is there a minimum length requirement?
- Could the approach be extended to handle hierarchical or structured user identification beyond simple integer keys?
- What is the impact of vocabulary size on the method's performance?
- How does the method handle adversarial attacks beyond simple insertion/deletion?

### Soundness
2

### Presentation
1

### Contribution
2
