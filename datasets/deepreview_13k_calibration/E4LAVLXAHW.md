# Black-Box Detection of Language Model Watermarks

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8

## Abstract
Watermarking has emerged as a promising way to detect LLM-generated text, by augmenting LLM generations with later detectable signals. Recent work has proposed multiple families of watermarking schemes, several of which focus on preserving the LLM distribution. This distribution-preservation property is motivated by the fact that it is a tractable proxy for retaining LLM capabilities, as well as the inherently implied undetectability of the watermark by downstream users. Yet, despite much discourse around undetectability, no prior work has investigated the practical detectability of any of the current watermarking schemes in a realistic black-box setting. In this work we tackle this for the first time, developing rigorous statistical tests to detect the presence, and estimate parameters, of all three popular watermarking scheme families, using only a limited number of black-box queries. We experimentally confirm the effectiveness of our methods on a range of schemes and a diverse set of open-source models. Further, we validate the feasibility of our tests on real-world APIs. Our findings indicate that current watermarking schemes are more detectable than previously believed.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper shows that it is possible to detect the presence of most existing watermarks using black-box interaction with the model, without knowing the watermarking key.
They also demonstrate that their attack is capable of estimating the parameters used in the watermarking schemes.

### Strengths
A huge number of watermarking papers have come out recently.
Many of them ask whether their watermarks harm generation quality by performing experimental evaluations, but these are inherently limited: There is no way to experimentally guarantee that the watermark will preserve the quality under *every possible* use-case of the model.
Therefore, perhaps a more useful test of quality is to simply attempt to detect it. If attacks that are specifically designed to detect the watermark still fail to do so, then this can be seen as unusually strong evidence that it is quality-preserving.

This work shows that existing schemes typically fall short in this respect, demonstrating an important weakness.

### Weaknesses
It is not surprising that they were able to easily detect the schemes they attacked. Those schemes are not designed to be undetectable.
In the "Limitations" section, they justify the choice to only consider these schemes with the claim that the provably-undetectable schemes "lack experimental validation" and "are not yet practical due to slow generation speed."

However, I believe these claims require justification because:
- "Excuse me, sir? Your language model is leaking (information)" is a practical implementation of an undetectable scheme. The author doesn't report any issues. This seems to already contradict the above claims.
- As I understand it, the generation speed of these techniques (including the one just mentioned) is _no slower_ than it is for any other scheme. They work essentially identically to other schemes, except that they are careful not to embed bias in cases where it might be noticeable without the key.
- I think that the reason there are relatively few practical demonstrations of undetectable schemes is just that most people doing experiments don't care about it. If you can get slightly better robustness by dropping undetectability, most experimentalists will go for that. However, since the message of the present paper depends on it _actually being difficult_ to build a practical undetectable scheme, it would be much more compelling if you at least attempt to do so.

Here is a simple undetectable scheme that you could try as a benchmark: Use Aaronson's scheme exactly (implemented in many places, e.g. Piet et al.), except that if a $k$-gram has empirical entropy (as defined in Christ et al.) less than $\lambda$, then don't use the Gumbel-max trick and instead just sample without bias according to the model. (Crucially, the first $k$ tokens in any response should be sampled exactly according to the model, without any watermark bias.) Note that this scheme is no slower than any other scheme. Detection with the key is also extremely fast.

It is easy to see that this scheme will require seeing roughly $2^{\lambda/2}$ tokens before it becomes detectable _without_ the key; and it should be detectable _with_ the key as long as the text has (empirical) entropy at least $\lambda$ in most sequences of $k$ consecutive tokens.
- If you find that this scheme only becomes practically undetectable once you set $k$ or $\lambda$ to be unreasonably large (such that detection with the key significantly suffers), then I would find the message that existing practical schemes much more compelling.
- If you find that this scheme is in fact practically undetectable for reasonable choices of $k$ and $\lambda$, then that would arguably be an even more compelling result (although the message would change slightly).

### Questions
In Appendix C, you discuss a method for estimating scheme parameters. Are your techniques capable of learning the watermarking key itself?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a black-box detection method for identifying whether a watermark is embedded in a Large Language Model (LLM). In this paper, the detectability of current watermarking schemes is investigated for the first time in a practical black-box environment. The researchers developed statistical test methods to detect the presence of watermarks and estimate parameters using a limited number of black-box queries for three popular families of watermarking schemes; Red-Green, Fixed-Sampling and Cache-Augmented. Experimental results show that these approaches are effective and cost-efficient across multiple open source models and different settings. The paper also discusses the ethical implications of its work, highlighting the benefits of raising awareness of the ease of detection of watermarking schemes, despite the potential risk of misuse.

### Strengths
1. This paper, for the first time, examines the detectability of current watermarking schemes in a practical black-box setting, which is practical in the real detection scenario.
2. The method is well written and the method makes sense and is easily understood. Each method has a clear section structure. 
3. The experimental results in the black-box scenario verify the effectiveness of the method.

### Weaknesses
1. Although the authors pointed out that their motivation is to study the ability of current watermarks to resist detection, they did not highlight the significance of watermark detection in real scenarios. Providing specific application scenarios of black-box watermark detection can help readers better understand the contribution of black-box watermark detection.

2. The results in Table 1 indicate the method in the paper is constrained by the need for distinct detection techniques for various watermarking methods, with poor generalization among them. As more watermarking methods are proposed, this may increase the cost of detecting watermarks.

3. Minor concern: Watermark detection results in Table 2 for production-level language models accessed via API are suboptimal and you can not conclude on the presence of a watermark,  which brings some concerns to readers about real-world detection.

### Questions
1.	Can you discuss more application scenarios of watermark detection? This question has a great impact on the contribution of the paper.

2.	Can you discuss potential commonalities between their detection techniques for different watermarking families? The universality of watermark detection technology is beneficial to reducing detection costs.

3.	Can the authors discuss more about why current detection methods are unable to determine the watermarking method of real-world production-level LLMs?

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
5

### Summary
The authors introduce statistical tests for detecting three main watermark families under blackbox setting, namely, Red-Green, Fixed-Sampling, and Cache-Augmented watermarks. They confirm the effectiveness of their methods in an extensive experimental evaluation across seven schemes and five open-source models, and execute them on three deployed models.

### Strengths
This paper suggests that current watermarking schemes may be susceptible to detection in the black-box setting and verify it in their experiments.

### Weaknesses
- This paper lacks a clear mathematical presentation of its algorithms, and the descriptions are often vague.

- The detection tasks for Fixed-Sampling and Cache-Augmented watermarks are trivial, and the proposed simple algorithm can be easily defended against.
  1. The detection algorithm based on unique outputs is not practical. In real-world applications, one can simply skip the first few tokens to ensure that generated outputs are different, which has been proposed in Algorithm 3 in Christ et al, 2024[1].
  2. The detection algorithm focused on cache is not applicable. It could take too much time for the detection to complete in waiting for the cache to be reset in a global cache. While user cache is usually not applicable due to a potentially large number of users.
  3. The cache mechanism is only a minor component of these watermarking schemes, and removing it often does not degrade performance, as discussed in Hu et al., 2023[2].


- Reporting median p-values over 5 watermarking keys is impractical, as only a single watermarking key is typically used per model in real-world applications.

The median p-value is not a good metric, as it does not reflect the actual false positive rate. It is also difficult to interpret.

- As shown in Figure 3, there are large deviations from the actual $\delta$, indicating that the current results may not be suitable for downstream tasks.

### Questions
1. The key algorithm for calculating the p-value in lines[197-240] is too vague. Could you please clarify it?

2. Could you provide a false positive rate for your detection algorithms? Additionally, the false positive rate may increase as we need to test various different types of watermarking schemes.

3. Could you provide a detailed algorithm for estimating the context size as described in lines[781-791], along with the corresponding experimental results?

### Soundness
3

### Presentation
2

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
This paper presents a significant contribution to the field of LLM watermarking. From the authors' claims, they are the first to provide a comprehensive study of black-box watermark detection. Their findings demonstrate the practical detectability of prominent watermarking schemes, challenging previous assumptions about their undetectability. This paper has provided the foundation for future research on more robust watermarking techniques and advanced detection methods.

### Strengths
This paper is extremely well-written. Kudos to the authors for taking time to ensure that the paper is concise, clear, and enjoyable enough for anyone to read. The formulations for each statistical test for detectability are clear and well explained. Providing detailed tests for each class of watermarks further strengthened the paper. The results highlight the strength of their approach as watermarks can be detected accurately, more so at a low cost. I also appreciate the fact that they experimented to see if their tests could cross detect other watermarks.

### Weaknesses
- The methods, while detailed, appear to focus on a strict reverse engineering approach for detecting each specific class of watermark. Did the authors explore the possibility of a unified approach that could detect all classes of watermarks? What are the authors' thoughts on this?

- The experiments were limited to just three classes of watermarks. I believe this is okay, and future work could expand the scope to include other types, but it is a weakness for this paper.

- The cross-detection tests only applied to watermarks from different classes. However, there were no evaluations on whether the detection is robust to variations in the hyperparameters of the same watermark. Can the detection identify a watermark regardless of the hyperparameters used?

- Additionally, the paper lacks details on the efficiency of the detection tests. For instance, how many tokens are required to reliably detect the presence of watermarks using these methods? Addressing this could further minimize costs.

### Questions
My questions are outlined in the weaknesses mentioned earlier. Please address those and the following:

- In transitioning from an attack-focused approach to a defensive one, do the authors believe that their tests would still be effective in detecting the presence of watermarks in texts that have been adversarially manipulated to remove them, especially in a blackbox scenario?

### Soundness
4

### Presentation
4

### Contribution
3
