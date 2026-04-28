# A Watermark for Black-Box Language Models

- Decision: Reject
- Avg Score: 4.60
- Scores: 6, 3, 5, 6, 3

## Abstract
Watermarking has recently emerged as an effective strategy for detecting the outputs of large language models (LLMs). Most existing schemes require \emph{white-box} access to the model's next-token probability distribution, which is typically not accessible to downstream users of an LLM API. In this work, we propose a principled watermarking scheme that requires only the ability to sample sequences from the LLM (i.e. \emph{black-box} access), boasts a \emph{distortion-free} property, and can be chained or nested using multiple secret keys. We provide performance guarantees, demonstrate how it can be leveraged when white-box access is available, and show when it can outperform existing white-box schemes via comprehensive experiments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes an LLM watermarking scheme that is applicable in black-box scenarios, i.e., when the party watermarking the text does not have access to the sampling procedure, but also in standard white-box cases. The authors prove the distortion free property and the lower bound on AUC. Extensive experiments among else evaluate watermark TPR/FPR, text quality, and robustness under token replacement and paraphrasing.

### Strengths
- While it is based on a generalization of ideas from existing schemes, the exact scheme proposed is to the best of my knowledge novel. The authors do a good job of exploring different variants of the scheme (e.g., CDF) in a principled way. 
- The theoretical results are sound. I especially appreciate that Theorem 4.2 is carefully placed into context and analyzed for various input values to demonstrate its implications. 
- Experiments are very thorough, involve important aspects such as quality evaluation with LLM judges and paraphasing attacks, and explore various scenarios and scheme ablations, making interesting observations.
- Whitebox results seem convincing (up to some reservations below), making the case for significance.
- While I have some issues with the method section (see below), the theory and experiments parts of the paper are very well written.

### Weaknesses
As a meta point, the authors are using the 2024 style file and should update it to the latest version to avoid desk rejection. I understand that this is an honest mistake, but in particular the lack of usual line numbers is making it hard to refer to particular parts of the writeup.

The weaknesses of the paper are in my view:

(1) Limitations of the evaluation setup
- The authors recognize that AUC is not the most practically relevant metric yet resolve this by proposing a new metric (AUC below fixed FPR), instead of using the more standard TPR @ fixed low FPR. As this is instantiated with a still high FPR of 1% the metric is still dominated by results at impractical FPRs. Can the authors elaborate on the decision to introduce this metric? Do the authors believe a false positive rate of 1% is a practical setting for real-world deployment?
- Prior work (Kirchenbauer 2023b among else) has already shown that short texts such as those studied here (~300 tokens) are not robust to paraphrasing, while (passive adversaries that do not learn the watermark beforehand) start being much less able to remove the best variants of KGW at above ~600 tokens. Can the authors extend their evaluation to include this setting and demonstrate that their watermark is equally or more robust?

(2) Despite being the title and the central framing of the paper, the practicality of the blackbox watermark is underdiscussed and not well substantiated. Perhaps framing the paper around the whitebox variant would have been more convincing. Namely: 
- As authors say, it can be hard to control token lengths of chat API responses. Further, and more importantly, it is not always possible to prefill the first $k$ tokens of the assistant response. This implies that the variant where $k$ is equal to text length is the most practical for blackbox models, yet is not evaluated, and there is no detailed discussion of this. As already for $k=50$ we can at most get 70 pAUC, it is likely that the practical variant would either not obtain good results, or need very high $m$. 
- The limitation of the blackbox setting that could be more explicitly mentioned/analyzed is that $len/k * m$ queries are needed to produce 1 text. For the practical setting above with high $m$ this can be prohibitively expensive. 
- The baselines (PostMark and Yang et al.) are not evaluated, yet they study the exact same blackbox setup. Can the authors explain this decision? Baselines being costly does not seem like a sound rationale, as they could still be evaluated along with their cost, which can then be compared to the cost of the proposed watermark. 

(3) Minor writing issues around the method description. In particular Sec. 3 is quite dense and not very friendly to readers aiming to understand the high-level idea behind the watermark. For example, $u_t$ is simply introduced but its components could be explained more intuitively, perhaps even through an example or supporting figures which are notably missing. Detail: $g(w)$ is introduced but not used later.

### Questions
All questions I list here are repeated from the "Weaknesses" section above:
- Can the authors elaborate on the decision to introduce the AUC until fixed FPR metric?
- Do the authors believe a false positive rate of 1% is a practical setting for real-world deployment?
- Can the authors extend their paraphrasing robustness evaluation to include longer texts and demonstrate that their watermark is as robust as best variants from prior work?
- Can the authors comment on the discrepancy between the blackbox-focused framing of the earlier sections of the paper, and the key results demonstrated and discussed in Sec. 5 being in the whitebox case?
- Can the authors comment on the statement that $k$ below text length $L$ is not as practical in the blackbox case, and include some experiments in the $k=L$ case?
- Can the authors compare their method to cited blackbox baselines or explain why this is not feasible?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
A method of generating watermarked text using query access to a language model is described.
The method works by auto-regressively sampling short sequences of tokens, selecting the sequence with the highest watermark score.
The watermark score is similar to Aaronson's.

### Strengths
The paper seems to do a good job of optimizing both their scheme, and the schemes they compare against.
In particular, it is interesting that making the watermark detector of Aaronson length-aware improves performance as much as it does.

### Weaknesses
The ideas and method are straightforward adaptations of existing work.
The technique is essentially identical to Aaronson's, except that they use rejection sampling instead of the Gumbel-max trick.
The scheme is also only distortion-free under certain assumptions about the text, which essentially translate to it having consistently high entropy.
This condition on distortion-freeness is extremely complicated. It doesn't actually help us understand what the condition is.
The fact that this does not "essentially translate to it having consistently high entropy" actually makes things significantly worse; my understanding previously was that at least I understood roughly when it would induce distortion, but now I am not sure.
And the scheme of Christ, Gunn, and Zamir (2024) is distortion-free under no assumptions about the text.

### Questions
The "Related Work" section appears to suggest that Aaronson and Kirchenbauer et al. were the first to embed information in LLM outputs.
However, the paper "Neural Linguistic Steganography" did this as early as 2019.

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a method for watermarking language models in a black-box setting. It only requires sampling output sequences from language models.

### Strengths
The method is effective in a black-box setting. It only requires to sample sequences from LLMs.

The paper provides formal guarantees for detection performance.

### Weaknesses
The paper’s motivation could be articulated more clearly. The main motivation stems from the security risks associated with providing API access that exposes logits to third-party users for applying their own watermark. However, simpler methods could enhance security; for instance, instead of exposing logits, LLMs could offer APIs to gather specific information users want to integrate. Furthermore, the paper presents a zero-bit watermarking technique, which only detects whether a text is watermarked but cannot infer additional information from the watermark.

The paper could also benefit from a more comprehensive evaluation. For example, comparing the time complexity of the proposed method with baselines and providing examples of watermarked text would strengthen the paper.

### Questions
Could you provide an example of watermarked text?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, a black-box watermarking scheme for LLMs is proposed. The idea is to enable watermarking with only sampling access i.e., without requiring white-box access to a model’s next-token probability distribution. The scheme allows third-party users with API-only access to embed watermarks without altering the distribution of generated text, achieving a distortion-free watermark (generated content is indistinguishable from the original output). It supports multiple secret keys, making it possible for different users to watermark the same model recursively without interference. The authors also provide theoretical guarantees on detection performance, false-positive rates, and robustness against adversarial attacks.

### Strengths
- The paper shows a solid theoretical analysis of the proposed scheme, as well as the distortion-free property that was claimed, establishing that the watermarked text is statistically indistinguishable from the original model's output.  They also provide a lower bound on detection performance, connecting it to the entropy of the language model's output and the number of samples used.
- The experimental results presented in the paper support the theoretical claims and demonstrate the effectiveness of the proposed scheme.  The authors conduct experiments on two popular LLM models, MISTRAL-7B-INSTRUCT and GEMMA-7B-INSTRUCT, and show that their scheme is competitive with or even superior to existing white-box watermarking schemes in terms of detection performance, text quality, and perplexity.
- The paper explores the robustness of the scheme to adversarial attacks - the impact of random token replacement and paraphrasing attacks. While paraphrasing proves to be a significant challenge, the scheme shows resilience to random token replacement. This analysis of robustness provides a realistic assessment of the scheme's strengths and limitations in practical settings. 
- The proposed framework is versatile and allows for various extensions and adaptations. For instance, it can be applied recursively, allowing multiple users to watermark the same model without interfering with each other. The scheme can also be adapted for white-box settings when next-token probabilities are available.

### Weaknesses
 - Practicality: What do the authors mean when they claim their method enables end users with only API access to embed watermarks? I am unclear about the motivation behind this approach. Is it practical for users to watermark a model that they do not own? What is the reasoning here, particularly if watermarking serves as a security measure to prevent model misuse? Wouldn't this imply that the method could also allow potential attackers access to the watermark?
- Experiments and General Format of the Paper: The paper lacks clarity and structure, making it difficult to fully grasp the motivation behind the proposed approach. While there may be a valuable contribution here, the current format obscures its impact. Figures and tables are largely separated from the sections where they are referenced; it would improve readability to place these closer to the relevant results. The theoretical guarantees could be moved to the end or even to an appendix, allowing more space for additional results in the main body. The motivation behind the approach needs clearer explanation—if the goal is to "give power back to the people," it should clarify why this is relevant, considering that users are not model owners, and watermarking aims primarily to prevent misuse. A well-articulated motivation would strengthen this section. Section 5.3 isn't necessary and could be integrated into the experimental results or discussion rather than standing as a separate section (optional).
- Results: The results presented are somewhat unconvincing. My primary baseline for comparison is KB, the initial paper to propose watermarking for LLMs. Although this approach targets black-box settings while aiming to remove distortions, it does not outperform KB, which was introduced nearly two years ago. Could the authors provide further insight into this? This issue may partly relate to the paper's structure, but I believe the authors need to highlight their main advantage more convincingly. For instance, it would be helpful to illustrate the tradeoff between distortion and text quality by comparing texts generated by KB and the proposed method, possibly using LLM-Judge. Additionally, if feasible, demonstrating the tradeoff between distortion and robustness would add value to the analysis.
- Finally, regarding the distortion-free claim, while the theoretical guarantees support this assertion, it would be beneficial to include qualitative results that demonstrate the distortion-free nature of the approach. Consider displaying examples of the unwatermarked text, the text watermarked by the proposed approach (using optimal hyperparameters), and the text watermarked by KB (also with optimal hyperparameters) for a clear, comparative illustration.

### Questions
Questions are in weaknesses above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents watermarking schemes for LLM’s outputs, in the setting that we only have black-box access to the model’s “next token generation” function.

They claim their scheme is “distortion free” and “can be used in a nested way”.

In a bit more detail, the paper’s scheme is based on a scoring function, which in turn is based on a secret key. Then, when the LLM’s output is being generated, at each step, multiple samples are gathered. Then, the scoring function is applied to them all and the one with the highest score is chosen.

### Strengths
The problem of black-box watermarking is an important problem, and having new schemes in this direction would be interesting. However, as I explain below, the schemes should be clear in what they offer and what is their advantage over previous work.

### Weaknesses
The main weakness of the paper is that it is barely readable, when one actually wants to understand the scheme and the arguments. The presentation of the scheme is super dense and lacks formality. Instead of introducing ideas one by one, they are jammed and one gets no intuition as to what is goin on, beyond the high level description of “using scores”.

In fact, the paper’s main setting (which seems to be the main novelty) is already used in previous work published in learning venues. For example, this (cited work) from more than year ago (published in COLT) https://eprint.iacr.org/2023/763 exactly studies the setting that the paper does: black-box access to the token generation function, and does use a similar idea of using a hash function to pick the next token by rejecting some. It is also provably robust (under certain conditions) as opposed to the weaker model studied here (random substitution) and comes with clear theorems that prove undetectability (which implies distortion free-nes and utility both).

One main comment for improving the writing:

- Try to define everything formally and at the right pace.
- There are also issues with using crypto terms without clarity. For example, F is a CDF, and then F[s] is a “single draw from a pseudorandom number generator for F seeded by integer seed s” .  I know cryptography well, but I have no idea what this sentence means. Then, it is assumed that F[h(K,w)] is a PRF. What is the citation that this is a PRF whenever F is PRG? (I don’t think this is true actually).
- What is the role of n-gram, l-gram, and their relation with tokens. Sentences like “where we allow the left endpoint to spill over only to…” are super informal and cannot be formally understood and checked.
Theorem 4.1 : what is F, and why should it be continuous? When it comes to efficient algorithms none are actually continuous (everything is discrete) so this is a strange assumption to make.

### Questions
My main question is about the novelty of the paper’s setting and its final results. As mentioned above, the work Christ et al already presents provably secure distortion free black-box watermark that is also robust to adversarial attacks (under a formal definition). Can you compare your work with them (and perhaps other similar previous works using crypto and rejection sampling) and explain what exactly the set of features that your work adds?

### Soundness
2

### Presentation
1

### Contribution
1
