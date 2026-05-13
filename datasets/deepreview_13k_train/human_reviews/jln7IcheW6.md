# Pseudo- vs. True-Randomness: Rethinking Distortion-Free Watermarks of Language Models under Watermark Key Collisions

- Decision: Reject
- Scores: 5, 3, 5

## Abstract
Language model (LM) watermarking techniques inject a statistical signal into LM-generated content by substituting the random sampling process with pseudo-random sampling, using watermark keys as the random seed. Among these statistical watermarking approaches, distortion-free watermarks are particularly crucial because they embed watermarks into LM-generated content without compromising generation quality. However, one notable limitation of pseudo-random sampling compared to true-random sampling is that, under the same watermark keys (i.e., key collision), the results of pseudo-random sampling exhibit correlations. This limitation could potentially undermine the distortion-free property. Our studies reveal that key collisions are inevitable due to the limited availability of watermark keys, and existing distortion-free watermarks exhibit a significant distribution bias toward the original LM distribution in the presence of key collisions. Moreover, we go beyond the key collision condition and prove that achieving a perfect distortion-free watermark is impossible. To study the trade-off between watermark strength and its distribution bias, we introduce a new family of distortion-free watermarks--beta-watermark. Experimental results support that the  beta-watermark can effectively reduce the distribution bias under key collisions.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
LLM watermarking use pseudorandom sampling to embed statistical signals into generated content without distorting quality. However, key collisions in pseudorandom sampling can lead to correlations that undermine this distortion-free property. The author show that key collisions are unavoidable and cause existing watermarks to bias towards the original LLM distribution. They prove that a perfect distortion-free watermark is unattainable and introduce beta-watermarks, which effectively reduce distribution bias under key collisions.

### Strengths
The paper is well written and the contributions are clear. It is nice to have a paper that clearly states what "distortion-free" can mean for LLM watermarks,  what are the implications etc. The math proofs looked correct to me.

### Weaknesses
The paper concludes that creating a fully distortion-free watermark is impossible because of key collisions. This result appears aligns with expectations, and it may not hold significant interest for the LLM watermarking community.


In particular, the importance of strongly distortion-free watermarks remains unclear. The authors suggest that a non-distortion-free watermark would result in repetitive generations. However, this issue also arises without watermarking when using greedy decoding. Furthermore, Aaranson et al. employ random decoding on top of the modified distribution of the next token, not just greedy decoding, which is the sole focus of the discussions regarding Aaranson et al. In such cases, repeatedly prompting a model with the same input does not necessarily produce identical outputs. Is this understanding correct?

See weaknesses.
- "Our studies reveal that key collisions are inevitable due to the limited availability of watermark keys, and existing distortion-free watermarks exhibit a significant distribution bias toward the original LM distribution in the presence of key collisions." -> What do the authors mean by "towards the original LM distribution?"

### Questions
See weaknesses. 
 - "Our studies reveal that key collisions are inevitable due to the limited availability of watermark keys, and existing distortion-free watermarks exhibit a significant distribution bias toward the original LM distribution in the presence of key collisions." -> What do the authors mean by "towards the original LM distribution?"

### Soundness
3

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
The authors propose three levels of distortion-freeness in watermarks, step-wise, weakly, and strongly distortion-freeness. They also argue that key collisions are inevitable in watermark generation, and then proceed to show that under key collisions, existing watermarks are not strongly distortion-free and confirm it as an impossibility result in theory. They also propose a metric for detecting watermarked models. Finally, they propose a new family of watermarks, and show that it is weakly distortion-free and performs better than existing ones on benchmark datasets.

### Strengths
1. The problem studied in this paper is important and it is also a timely topic. As the authors have argued, key collisions are inevitable, then how to resolve the problem brought by key collisions in watermarks is an important problem to study. 
2. Exploiting true randomness within the usage of pseudorandom keys is a good insight for designing watermarks.

### Weaknesses
This paper is composed of two parts, proofs and claims on distortion-free watermarks and a new solution for weakly distortion-free watermarks. Both parts have limited contributions. See below for more details.
1. The technical merit is limited. The claims in this paper are rather easy to prove (yet the notation is quite heavy). E.g., Theorem 4.13 is pretty straightforward. A model with detectable watermarks and the same output distribution as the original one does not exist.

2. I do not understand the motivation for detecting watermarked models. Why not detect watermarked texts? The service provider knows which models (they provide) are watermarked in the first place, and the task is to determine which texts are generated from the watermarked models they provided (for copyright, intellectual property, plagiarism detection, etc.). Hence, theorem 4.12 (although it is technically valid) also does not make sense to me. Why would the service provider compute the performance metric for two models that she/he has access to and determine if one of them is watermarked? 

3. The proposed solution ($0<\beta<0.5$) is similar to the permute-reweight baseline ($beta=0$). The novelty is limited and the performance increase (shown in Table 2) is marginal (compared with $beta=0$). 

4. The experiment section is limited. The baselines are limited to distortion-free baselines and statistical watermarks are not included.

5. It is important to show that distortion does lead to worse performance in watermarked models, otherwise distortion-freeness is not well-motivated. Without this motivation, this paper is mainly proposing a new solution for distortion-free watermarks, and given that the solution does not seem novel, the contribution of this paper is limited.

6. From Figure 3, it is not clear which watermark performs better. Is there any direct measurement of the distortion-freeness?

### Questions
1. Address the above weakness section, especially W4, W5, W6, W2.
2. There are some typos. E.g., in line 60, ``In particular`` should not be capitalized.

### Soundness
3

### Presentation
2

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
This paper explores the application of pseudo-random and true-random sampling in distortion-free watermarking for language models, highlighting that pseudo-random sampling may introduce distributional bias under watermark key collisions, thereby affecting watermark quality. The paper proposes a beta-watermark method, which balances watermark strength and distributional bias to mitigate collision-induced bias, enhancing detection efficiency.

### Strengths
1. This paper investigates the impact of pseudo-random versus true random sampling on watermarking applications, offering a valuable contribution to the field.
2. The paper provides a rigorous proof that strongly distortion-free watermarking algorithms are theoretically unattainable. Theoretical proofs are well-aligned with experimental results, supporting the paper’s main conclusions.
3. The proposed trade-off method between watermark strength and model performance demonstrates practical flexibility and applicability in specific scenarios.

### Weaknesses
1. The proposed beta-watermark shares considerable similarities with DiPmark (Yihan Wu, Zhengmian Hu, Hongyang Zhang, and Heng Huang. Dipmark: A Stealthy, Efficient and Resilient Watermark for Large Language Models), as both are variations of the permute reweight PDA-rule. Additionally, the algorithms in Appendix A are nearly identical to Algorithms 1 and 2 in DiPmark. It is recommended to add a comparison with DiPmark in the paper.
2. The experiments primarily compare against soft watermarking (ICML 2023 Best Paper) but lack examples of comparing watermark text effects under different parameters. Furthermore, it is recommended to include comparisons with other watermarking techniques mentioned in the paper to enhance understanding for the audience.
3. The paper does not analyze or compare watermark detection time, algorithmic complexity, or system performance overhead.
4. The paper analyzes the performance of the watermark model under key collisions, which reflects the issue of information capacity in watermarking algorithms. However, typical applications of text watermarking have low demands on key space, and the paper lacks a clear positioning of its problem setting. The paper uses identical prompts producing identical outputs to illustrate randomness issues, but this randomness is model parameter-dependent and unrelated to the watermarking algorithm.
5. The differences between Figures 4 and 6 are minimal. It is recommended to combine the different line plots into a single figure for comparison.

### Questions
1. Section 4.3 of the paper designs a black-box, distortion-free watermark detection algorithm that relies on comparisons with the original unwatermarked model. However, no comparative experiments are provided in the paper. What advantages does the proposed detection algorithm offer, and would it provide any efficiency improvements?
2. The experimental data only presents results with δ values greater than 1, in comparison to the reference Soft watermarking paper. However, no data is provided for δ < 1. Would the proposed method still demonstrate an advantage under δ < 1 conditions? Please provide relevant experimental data.
3. The discussion on pseudo-random versus true random sampling could be further expanded, with a more in-depth analysis on the specific impact of different pseudo-random algorithms on distribution bias.

### Soundness
2

### Presentation
3

### Contribution
2
