# Watermarking using Semantic-aware Speculative Sampling: from Theory to Practice

- Decision: Reject
- Scores: 5, 8, 6, 5

## Abstract
Statistical watermarking offers a theoretically-sound method for distinguishing machine-generated texts. In this work, we first present a systematic theoretical analysis of the statistical limits of watermarking, by framing it as a hypothesis testing problem. We derive nearly matching upper and lower bounds for (i) the optimal Type II error under a fixed Type I error, and (ii) the minimum number of tokens required to watermark the output. Our rate of $\Theta(h^{-1} \log (1/h))$ for the minimum number of required tokens, where $h$ is the average entropy per token, reveals a significant gap between the statistical limit and the $O(h^{-2})$ rate achieved in prior works. To our knowledge, this is the first comprehensive statistical analysis of the watermarking problem. Building on our theory, we develop **SEAL** (**S**emantic-awar**E** specul**A**tive samp**L**ing), a novel watermarking algorithm for practical applications. SEAL introduces two key techniques: (i) designing semantic-aware random seeds by leveraging a proposal language model, and (ii) constructing a maximal coupling between the random seed and the next token through speculative sampling. Experiments on open-source benchmarks demonstrate that our watermarking scheme delivers superior efficiency and tamper resistance, particularly in the face of paraphrase attacks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper contains two independent contributions:

The theoretical analysis provides a treatment of watermark strength in terms of Type I and II errors, discusses the best watermark in the minimax sense, i.e., how much Type II error can be achieved while ensuring Type I error is bounded, and the optimal watermark detection method to achieve it, both when the model distribution is known and when it is unknown but has a bounded probability (so the probability is sufficiently non-concentrated). It then explores the minimum number of tokens needed to achieve bounded Type I and II errors in both iid and non-iid settings.

The practical SEAL method introduces an additional proposal model and assumes its output distribution is known. It uses maximal coupling to couple the proposal and target models during generation, similar to speculative sampling, and uses the proposal model's output distribution for detection.

### Strengths
Provides a theoretical treatment of watermark strength in terms of Type I and II errors.

Derives minimax optimal watermarks and detection methods under different knowledge assumptions about the model distribution.

Gives bounds on the number of tokens needed for effective watermarking in various settings.

Proposes the SEAL method that leverages a proposal model.

### Weaknesses
1. Insufficient comparison with related semantic-aware watermarking methods:

The paper cites several semantic-aware watermarking methods, such as:
-  "Watermarking Conditional Text Generation for AI Detection: Unveiling Challenges and a Semantic-Aware Watermark Remedy", which uses a word similarity matrix
- "SEMSTAMP: A Semantic Watermark with Paraphrastic Robustness for Text Generation" and "k-SemStamp: A Clustering-Based Semantic Watermark for Detection of Machine-Generated Text", which use locality-sensitive hashing
- "A robust semantics-based watermark for large language model against paraphrasing", which uses Normalized Embedding Ring (NE-Ring)

All these methods seem to better capture semantic information compared to the random hash functions used in this paper. However, the paper does not provide any discussion or comparison with these cited works. The random hash functions and other designs in SEAL are hard to justify as capturing semantic information. More details in point 6 below.

2. Lack of rigor in theoretical proofs:

- In the proof of Theorem C.2, in line 1435, authors claim "third inequality is achieved when $\sum_{x\in\Omega:\rho(x)<\alpha}\left(\alpha-\rho(x)\right)\geq\epsilon$. a sufficient condition for which being $|\Omega|\geq1/\alpha $".

However, this is clearly not a sufficient condition as it is missing an ϵ term. The condition should be more precisely $|\Omega| \geq (2+\epsilon)/\alpha$ to ensure the inequality holds. The current condition is too weak.

- In Theorem C.14, in line 1888, the proof uses a new condition $m:=|\Omega|\gtrsim1/\kappa$ or equivalently $n\log|\Omega_0|\gtrsim\widehat{H}$ which was not given in the theorem statement. The introduction of this condition mid-proof without prior mention in the theorem statement makes the result difficult to interpret and verify.

- Again, in Theorem C.14, line 1893, it applies the result of Theorem C.6 without ensuring its conditions are met. The proof does not explicitly check if the required conditions of Theorem C.6 are satisfied before applying its result, which is a critical oversight.

- Again, in Theorem C.14, line 1912, the proof is omitted with the authors claiming "some arithmetic shows". However, the steps are hard to establish. It is unclear how to verify the first inequality
$\max\{\frac{\binom{m-\frac{\rho(\bar{\Omega})}{\kappa}}{\alpha m}}{\binom{m}{\alpha m}}-\rho(\bar{\Omega}^{c}),0\}\leq\rho(\bar{\Omega})\cdot(1-\alpha)^{1/\kappa\_{0}}$
 without further explanation from the authors. The second inequality $\rho(\bar{\Omega})\cdot(1-\alpha)^{1/\kappa_0}\leq\beta\cdot\rho(\bar{\Omega})$ where $\kappa_{0}=\operatorname{log}\frac{1}{\alpha}+\operatorname{log}\operatorname{log}\frac{1}{\beta}$ has clear counterexamples, e.g., $\alpha=e^{-1}, \beta=e^{-e}, \kappa_0=2$ gives $(1-\alpha)^{1/\kappa_0}\approx 0.794$ and $\beta\approx 0.06599$. It is completely unclear how the proof proceeds. The definition of $\kappa_0$ also seems incorrect and should be $\kappa_0 = \alpha/\log(1/\beta)$.

- The Type I error bound for SEAL relies on a quantile of sum of Bernoulli random variables that are assumed to be independent, as stated in line 1242. However, this is impossible as the mean of $\xi_{i+1}$ at the $(i+1)$-th token depends on the proposal model's output distribution, hash function, and ultimately the prefix $t_{1:i}$, which is correlated with $\xi_i$. So they are not i.i.d. and this assumption cannot be used. While modeling as i.i.d. Bernoulli may be a convenient assumption that gives practical watermark detection criterion, it is not theoretically rigorous and should not be presented as a strict theorem but rather an educated guess.

- Additionally, Theorem G.5 is not rigorously stated. The assumption "When the sequence y is not generated by Algorithm 3, ξj 's are i.i.d. Bernoulli random variables" is too weak, as "not generated by Algorithm 3" itself does not imply any information. It is entirely possible to generate from a slightly perturbed version of Algorithm 3, in which case the theorem cannot possibly hold. The theorem should specify that the sequence y is fixed and the randomness comes from the proposal model's output.

3. Outdated and lacking experimental baselines:

   - Although the paper claims to "compare SEAL with one of the state-of-the-art watermarking methods, the exponential scheme (Aaronson, 2022b)", Aaronson's work is a pioneer work and definitely not the latest SOTA. The claim of it being SOTA is incorrect.

   - The paper completely lacks comparison with the semantic-aware methods listed above. These methods are relevant to SEAL as they all deal with the semantic-aware direction, which SEAL claims to do.

   - The paper also lacks comparison with model non-agnostic methods. Table 5 is made under the model non-agnostic setting, but all the compared works are model agnostic methods that do not actively utilize model probability information, which is misleading and unfair. It should have included existing model non-agnostic methods, such as:
     - The log likelihood ratio (LLR) test, which is the strongest test as discussed in "Unbiased Watermark for Large Language Models" and "A statistical framework of watermarks for large language models: Pivot, detection efficiency and optimal rules."
     - The Maximin variant of LLR score from "Unbiased Watermark for Large Language Models", which is a robust practical variant of LLR.

   - The lack of thorough review/comparison leads to an incorrect claim in line 97 that "previous rates on the number of tokens consistently fails to surpass $h^{-2}$", as the authors completely overlooked model non-agnostic methods (e.g. LLR) that already achieve the best detection efficiency.

4. Missing key experimental details:

   - The experiments lack error bars, which are important for readers to check what is signal and what is noise. It is hard to do so without reporting error bars.

   - When comparing exponential and SEAL, both are unbiased (distortion-free) in token distribution but the plotted quality differs a lot. If there are no implementation errors, this suggests a large variance that the authors should have clearly plotted. The errors are also missing in Table 1.

   - The experiments are suspicious. In Table 1, Exponential, Inverse Transform, Binary, and SEAL can all achieve unbiased (distortion-free) token distribution, but the quality differs drastically. It is reasonable to suspect issues with the experiments, but the authors do not provide code and there is no way to confirm.

5. Weak connection between the theoretical and algorithmic contributions:

   - The authors claim "This insight led us to develop semantic-aware random seeds, which adapt to the underlying distribution of the tokens." (line 264). However, Section 2 and the appendix do not mention any discussion about semantics, and the word "semantic" is not even mentioned. The connection between the theoretical analysis and the claim of semantic awareness is not clear.

   - The authors also claim "Second, our analysis of both Theorem 2.3 and 2.4 reveals ... and the pushforward of the token distribution onto the same measure space". This is not obvious from Theorem 2.3 and 2.4, which do not even mention the word "pushforward". Further explanation is needed on how the theory in Section 2 provides information about the pushforward measure. The theorems do not explicitly discuss the pushforward of token distributions.

   - There are many other mismatches:
     - Section 2 has a lot of discussion on Type II error, but Section 3 does not discuss Type II error at all. The practical algorithm does not address the theoretical analysis of Type II error.
     - The final result in Section 2 is deriving the optimal rate $h^{-1}\cdot\log(1/h)$, but Section 3 does not discuss whether this rate can be achieved. Reading the abstract, one would expect a new algorithm achieving the optimal rate, which would be an important progress, but there is no relevant discussion in Section 3. The paper does not demonstrate that the proposed method achieves the derived optimal rate.

   - It is unclear why Section 2 is related to Section 3. It seems like two independent contributions stitched together.

6. SEAL does not truly capture semantic information:

   - SEAL still operates on token distributions like traditional watermarks (but with a projection onto hash codes space with a random hash function). The hash functions, speculative sampling (maximal coupling) in this process do not handle semantic information such as distinguishing word similarities. Only the original language model and proposal model use semantic information when doing next word prediction. A watermarking method should not be called semantic-aware just because next word prediction $p(\cdot|x_{1:t})$ contains semantic information.

   - Examples of truly semantic-aware watermarking methods:
     - "SEMSTAMP: A Semantic Watermark with Paraphrastic Robustness for Text Generation" and "k-SemStamp: A Clustering-Based Semantic Watermark for Detection of Machine-Generated Text" use hash functions that consider semantic information.
     - "Watermarking Conditional Text Generation for AI Detection: Unveiling Challenges and a Semantic-Aware Watermark Remedy" combines semantically similar words when watermarking.
     - "A robust semantics-based watermark for large language model against paraphrasing" extracts watermark information from embeddings.
     
     All of these methods better capture semantic information compared to the random hash functions used in this paper.

   - In contrast, the random hash functions and speculative sampling in SEAL do not handle semantic information and should not be called "Semantic aware". The use of random hash functions does not inherently capture semantic relationships between words.

7. Writing issues:

   - Inconsistency between algorithm and figure: In the "Bootstrapping efficiency with logits bias" part, it is stated that a bias δ is introduced to the logits, but Figure 2 shows it being added in the maximal coupling step. The description of where the bias is added is inconsistent between the text and the figure.

   - Typos and undefined notations:
     - In line 812, G is not defined. The variable G is used without prior definition.
     - In line 825, C is defined but not used. It does not appear in the actual steps of the algorithm or the definition of the rejection region R. It is unclear why it is defined and what its purpose is. The variable C is defined but not used in the algorithm or detection process.

   - Confusing notation: $\eta$ is used to denote minimax in the main text (line 185, line 206) but used to denote probability in the appendix (line 785). The same notation is used for different concepts, which is confusing.

### Questions
1. Can the theorems and proofs be fixed?

2. How does SEAL's random hashing compare to prior locality-sensitive hashing, word similarity matrix, or Normalized Embedding Ring methods in capturing semantic information? Why is next word token prediction following random hash functions considered to capture semantic information?

3. Why is SEAL considered model-agnostic when it requires a language model's probabilities? If a watermarking algorithm generates watermarks using model M1 and detects watermarks using model M2, is it still considered model-agnostic?

4. Is there any deep connection between the Type II error theoretical analysis and SEAL? 
   - Half of the main text discusses the asymptotic number of required tokens, with the optimal rate being $h^{-1}\cdot\log(1/h)$. Can SEAL achieve this rate proposed in the paper? If so, why is there no theoretical proof? 
   - Or is it the same as all existing model-agnostic methods (like the exponential method), i.e., $h^{-2}$? 
   - The paper claims that the theoretical analysis guided the design of the new SEAL method. Does SEAL achieve any theoretical asymptotic bound improvements through this guidance?

5. With what probability is the hash function introduced in the SEAL algorithm not injective? 
   - If the hash codes space $\Omega_{h}$ is very large, is a random hash function injective with high probability? 
   - If it is injective, is the entire process equivalent to normal speculative sampling? 
   - If the hash function step is skipped and speculative sampling is performed directly on token space, will the watermark strength be stronger? 
   - Why introduce this extra hash step?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper makes two main contributions: 1) it establishes (essentially) matching asymptotic upper and lower bounds on watermark statistical power (in terms of the number of tokens required to detect the watermark), where the upper bound is substantially stronger than previous work; and 2) it develops a watermark inspired by this analysis and empirically validates its power. In both cases, the main idea is to assume some knowledge of the underlying watermarked language model (i.e., the token probabilities in the putative text) and incorporate this knowledge into watermark detection.

### Strengths
The paper proposes a watermarking scheme and provides both theoretical and experimental evidence arguing this scheme is stronger (in terms of statistical power) than prior work. In terms of the theory, the upper bounds established in the paper are notably stronger than prior work. The experimental results are more mixed: the watermark outperforms some prior work in some settings; however, it is good that the paper at least carries out experiments to validate the theory.

### Weaknesses
The comparisons (both theoretical and empirical) to prior work are arguably unfair for the following reasons: 1) the paper assumes knowledge of the watermarked language model (either directly or via a proxy proposal LLM) during detection, which prior work does not; and 2) the watermark generation procedure proposed by the paper appears to be more computationally intensive than prior work (e.g., it involves using a proposal LLM and speculative decoding). 

If only for clarity reasons, it would be good if the paper could be more explicit about what trade-offs exist between their method versus prior work (both theoretically and empirically). Concretely, in terms of experiments, it would be helpful to 1) systematically vary the degree to which the proposal LLM differs from the original watermarked LLM and study the effects on watermark power and 2) benchmark the runtime of watermark generation compared to prior work.

### Questions
Are there any guarantees regarding the difference in the *joint* distribution over multiple samples of original versus watermarked text from the watermark proposed in the paper?

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
3

### Summary
This work makes two contributions: (i) a rigorous theoretical analysis of the statistical limits of watermarking and (ii) a new watermarking scheme named SEAL based on a maximal coupling between the random seed and NTP. SEAL was shown to be more efficient and tamper-resistant than some existing methods in the literature.

### Strengths
1. This work provides the first rigorous analysis of the fundamental limit of statistical watermarking. It addresses a few important questions of watermarking that are of theoretical interest.
2. The use of speculative sampling appears to be new and interesting in the current context.
3. The SEAL algorithms have been demonstrated to perform well compared to SOTA methods.

### Weaknesses
The paper can be strengthened by presenting the theoretical results in more realistic settings and elaborating more on how these results can be practically relevant. For instance, according to Theorem C.2, the UMP requires the rejection region $R$ to be a singleton set. Such a scheme is practically less useful (it is essentially a retrieval-based approach that involves keeping a growing record of all generated texts and checking for matches). The i.i.d assumption in Theorem 2.3 again makes the results impractical, as it does not hold in any real-world setting. Furthermore, the theoretical results ignore the prompts' impacts, which can significantly affect the next token distribution.
The paper lacks a detailed discussion of the proposed SEAL method's rationale and novelty. It would be particularly helpful to discuss its rationale and compare it with existing semantic-aware watermark schemes in the literature.

### Questions
1. Can the authors elaborate more about the role of the proposal LLM in their framework and how its quality affects SEAL's performance?  
2. When the proposal LLM is the target LLM and $\Omega_h=${0,1}, it appears that SEAL would reduce to the "green-red" list scheme in Kirchenbauer et al. (2023) with a proper choice of the hash function $h_i$. Can the authors make a more careful comparison with the "green-red" list approach along this line?
3. My understanding is that speculative sampling enhances computational efficiency, but it may not necessarily improve statistical efficiency or robustness. It would be helpful if the authors could provide intuitive explanations for how using the proposal LLM and speculative sampling improves the method's efficiency and resilience. What is the most essential component of SEAL that contributes to its statistical efficiency and robustness?
4. Given that SEAL is constructed based on maximum coupling, does it enjoy certain theoretical optimality regarding power/Type II error?
5. Please comment on the sensitivity of SEAL to the tuning parameters such as $K$, $\Omega_h$, and the hash function.

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
4

### Summary
This paper investigates methods for embedding watermarks in the outputs of large language models (LLMs). The study examines two types of errors in watermark detection: the first type being false positive errors, and the second type being false negative errors. The paper theoretically discusses the lower bound of the second type of error under the condition of a fixed first type of error. Furthermore, it considers the amount of output text required for embedding the watermark. Finally, the paper presents a construction for embedding watermarks in LLM-generated texts. This construction extracts the semantic information of the output text and uses this semantic information as the seed for generating the watermark, employing speculative sampling to embed the watermark into the subsequent output text.

### Strengths
1.The paper attempts to discuss the relationship between two conflicting errors in watermark detection, establishing a lower bound for the second type of error when the first type of error is fixed. This theoretical research is helpful for designing more effective watermark algorithms.

2.The paper attempts to use semantic information as the seed for the watermark, which could be an interesting idea. However, I am not sure what advantages this approach has over directly using the text as the seed.

### Weaknesses
1.The paper's construction uses semantic information generated by an LLM as the seed for generating the watermark. However, LLMs are generally probabilistic algorithms, meaning that even with the same prompt input, the outputs can vary between two different instances. If different texts are used as seeds, the resulting pseudo-random numbers will differ, leading to different secret keys as in Fig.2 and making it impossible to complete the watermark detection. This is a critical flaw because the watermark should be reliably detectable even with minor variations in the seed text. The paper does not adequately address how the system would handle these variations in semantic extraction, which could lead to a high false negative rate in practical applications.

2.The paper's discussion does not consider the impact of an attacker modifying the text. Even slight changes to the text by an attacker could affect the extraction of semantic information, which in turn would impact the watermark detection. This is a significant oversight, as any practical watermarking scheme must be robust against common adversarial attacks such as paraphrasing, synonym substitution, or minor reordering of sentences. The paper needs to address how the proposed method would maintain watermark integrity under such adversarial conditions. The lack of robustness against even simple attacks makes the method impractical.

3.The writing in the paper is not clear enough, as the embedding and extraction of the watermark are not explicitly expressed in algorithmic form, making it difficult to understand the construction details. The description lacks sufficient detail to allow for replication or thorough analysis. Without a clear algorithmic description, it is difficult to assess the practicality and effectiveness of the proposed method. The paper should provide a clear, step-by-step algorithm for both embedding and extraction processes.

### Questions
1. If the extracted semantic information is not completely consistent, will it result in watermark inconsistency? Will it affect the watermark detection?

2. On page 6,  h_i is a hash function, and in the subsequent description, there is an expression  h_i^{-1}(A) . What does  h_i^{-1}  mean? This form is generally considered an inverse function, but hash functions typically do not have inverse functions.

### Soundness
3

### Presentation
2

### Contribution
2
