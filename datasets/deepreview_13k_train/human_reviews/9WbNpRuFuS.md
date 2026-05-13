# Approximately Aligned Decoding

- Decision: Reject
- Scores: 5, 8, 5, 5

## Abstract
It is common to reject undesired outputs of Large Language Models (LLMs); however, current methods to do so require an excessive amount of computation, or severely distort the distribution of outputs.
We present a method to balance the distortion of the output distribution with computational efficiency, allowing for the generation of long sequences of text with difficult-to-satisfy constraints, with less amplification of low probability outputs compared to existing methods.
We show through a series of experiments that the task-specific performance of our method is comparable to methods that do not distort the output distribution, while being much more computationally efficient.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a method to speed up the recently proposed ASAp algorithm for constrained decoding by leveraging a connection to speculative decoding. This connection relaxes the exactness of the decoding algorithm, but improves the efficiency of decoding. ASAp iteratively samples a prefix from an LLM until it finds that the prefix violates a constraint, in which case it stores the prefix in a "bad set" B and restarts generation. Instead of restarting the generation in this step, this paper proposes reusing partial prefixes that don't violate the constraint, inspired by speculative decoding. Compared to rejection sampling at one extreme and greedy constrained decoding at the other, the authors show that proposed algorithm (AprAD) occupies a useful midpoint on the tradeoff between computational efficiency and faithfulness to the true posterior distribution $p(response | constraint)$.

### Strengths
- By relaxing the exactness of ASAp and leveraging a connection to speculative decoding, AprAD is faster than rejection sampling / ASAp but produces much higher-quality outputs than greedy constrained decoding on the two empirical settings (generate without using a particular letter + code generation without hallucinated API calls).

- The authors use a synthetic setting to test how much AprAD distorts the output distribution compared to ASAp and greedy constrained decoding, and find that AprAD results in much lower divergence to the true distribution than constrained decoding and much more efficient decoding (in terms of model evaluations) than ASAp.

### Weaknesses
 - Regarding posterior estimation approaches, it's not explained in detail what "Both of these methods...also face issues in certain dense error sets—the approximation of the posterior tends to become inaccurate when arbitrary generations almost immediately lead to an error." means. The paper needs to back this claim up with experiments, and it's still worth comparing to these methods.

- The proposed constraints in the experiments are somewhat arbitrary and differ from examples in other constrained decoding work. For example, why not evaluate on the same tasks as ASAp?

- The paper is missing a citation and comparison to a very simple decoding method that tries to solve the same problem with greedy constrained decoding: [FUDGE](https://aclanthology.org/2021.naacl-main.276.pdf).

- Membership in $\mathcal{B}$ has to be determinable by any prefix, which is not a limitation of other methods (such as FUDGE, and the posterior estimation methods cited in the paper.) In fact, this very assumption should fit FUDGE very well.

- It's stated that the main weakness of ASAp is "While ASAp succeeds in cases where there are only a small number of errors that comprise
the majority of the probability mass, its generation speed suffers when there are a large number of errors—each error must be discovered before it is added to $B$. In dense probability sets, its performance characteristics are similar to rejection sampling, as there are an exponential number of error sequences that must be discovered as generation length increases." 
But doesn't the proposed method have the same drawback, in the sense that every generation violating the constraint must be discovered before it's added to $B$? The decoding *speed* should be better, but the doesn't the fact remain that in the limit of many samples, both methods explicitly store every prefix violating the constraints?

- Related to the above points, the cited weakness of the posterior estimation approaches is cases "when arbitrary generations almost immediately lead to an error". But aren't those also precisely the bad cases for ASAp and AprAD in terms of representing $B$?

### Questions
- L304--L309---why ask human raters about the intent of the constraint when many of these things (e.g., lookalike cyrillic characters, accented characters) could just be incorporated into the constraints by expanding the set of banned tokens?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The topic of this paper is how to efficiently generate text from LLMs such that the generated text avoids undesirable outputs. The paper is well written and gradually introduces the necessary concepts.

First, the authors introduce the trivial autoregressive generation of text token by token. Then they introduce speculative decoding which uses a LLM and a small speculative model (SSM). The introduction of the speculative decoding is necessary because the final method introduced by the authors use it. After this the authors describe the current methods and their drawbacks. They formalize the set of undesirable strings B (that can be of infinite size) and they require the property that, if a string x belongs to B (is undesirable) then all strings that have x as a prefix also belongs to B (is undesirable). This is assumption might require a careful design of B (see lines 94-98 for the discussion). First, the rejection sampling is introduced - a sampling where we sample the text and resample it until it generates a string not belonging to B. This might be expensive for obvious reasons - when the most generated strings happen to be in B, we have to resample many times. Then the paper introduces the constrained generation, where we generate as normal except, when the next symbol creates a string in B, we reject the symbol and consider only symbols that yield sequences not in B. As authors describe it, this can amplify unlikely generations because we commit to perhaps unlikely prefixes during the generation (lines 149-153). Then authors describe the method known as Adaptive Sampling with Approximate Expected Futures (ASAp) (Park et al., 2024), where the method keeps sampling until a bad sample is encountered. Then conditional probabilities are computed to avoid the bad sample and the process is repeated. The hope is that the encountered bad samples are much fewer than the entire set B and the process ends fast. This, however, might not happen especially when a lot of errors must be discovered and added to the bad sample set. The paper also introduces a somewhat related method of posterior estimation, which has been used in previous works.

Finally, the authors introduce their method (Approximately Aligned Decoding, or AprAD) which combines ideas from speculative decoding and ASAp. The main idea is that regular decoding and decoding where we condition out a bad sample are very close in distribution and speculative decoding can be used to sample from the conditional distribution.

### Strengths
The authors evaluated the proposed method on synthetic and real data. For the synthetic data, the authors consider sequences consisting of letter A, B and C.  They define various sets of error sets and measure the KL divergence between the distribution for optimal generation as well as other methods. Their method comes up top when considering the speed of generation (generation ratio which they define in the paper). The paper also considers experiments on more "real" data such as lipograms (texts omitting certain vowels) as well as bigcodebench hallucination avoidance.

The paper is very approachable for somebody not in the area as it introduces the notions in a gradual fashion. They study an important problem and give a very neat algorithm for it. I recommend the paper to be accepted at the conference.

### Weaknesses
please see summary

### Questions
Small comment: on line 199: what is DFA? Deterministic finite automata? It would be nice to define it.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focuses on the problem of constrained generation from autoregressive language models, where some prefixes are considered as error that should be excluded. Following this condition, the entire language model should be renormalized, in order to sample correctly. However, it is non-trivial to renormalize a language model in a huge sample space. Previous works either fail to renormalize, or require multiple rounds of trial-and-errors to produce a meaningful sample. The recently proposed ASAp falls under the second category. This paper improves ASAp by introducing backtracking into the sampling procedure, reducing the computational overhead while retaining some renormalization. The backtracking is technically the same as speculative sampling procedure, but uses the current language model as the speculative model. 

The experiments include analysis on synthesized dataset and evaluation on lipograms and hallucination avoidance tasks. All tasks show that while the proposed method, called AprAD, performs comparably to ASAp, it requires fewer number of model evaluations, thanks to the introduced backtracking procedure.

### Strengths
I feel that this paper is undersold given its current presentation. The proposed method will be useful, but I would not argue for acceptance now.
- This work tackles an important task of decoding from language models under constraints. The task is crucial for responsible and safe control of large language models. In practice, the downstream tasks, with their own safety or legal constraints, are usually developed separately from the training of the models. The proposed method explores effective modification of pretrained language models, which is an interesting topic in the larger picture.
- The ideas are clearly presented, with fair comparisons that support the claims. The discussion of related works defines the position of the ideas. Again, I think the proposed method is useful, and should published somewhere.

### Weaknesses
My main issue with the work is its presentation, which makes it weaker than it should be.
- Throughout the entire paper, the idea is presented as a combination of ASAp and speculative sampling. But I think it has its own merits that are different from speculative sampling. First, the main point of speculative sampling is parallelization but the proposed approach focuses more on backtracking. During the backtracking in this work, there is actually no need of evaluating the language models as the probability tables are already obtained. This leads to a completely different version of "speculative sampling". However, the differences are not discussed or presented in the manuscript. Second, the backtracking in this work always goes to the beginning. Combined with the sampling under ASAp, the actual algorithm is more complicated than its current form. It would be interesting to have a complete pseudocode of all related techniques. 
- In line 225, I think $\hat{P}^{B}$ is the speculative model and $\hat{P}^{B\cup \{x\}}$ is the target model. The two arguments should be swapped.
- The experiments are designed to meet the assumptions of the methods. It would be more interesting to include a real experiment that makes real impact.

### Questions
- In AprAD, are the probability tables that lead to the current decoding cached? Is the caching the main reason why it requires fewer evaluations of the language models?
- I imagine sometimes the user wants softer constraints and sometimes the user values faster generation. Is it possible to introduce hyperparameters to control the behaviors of the proposed approach?

### Soundness
4

### Presentation
2

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
This paper focuses on the constrained decoding (or completion) problem. The traditional per-token constrained decoding algorithm will violate the distribution, largely deviating from the ideal distribution;  the ASAp algorithm can solve this issue, but may need much computation. This paper proposes to use a per-token approximation of ASAp, which is called AprAD. The key idea is to keep the pre-sampled tokens as possible, and use speculative sampling to adjust the distribution (the Speculative sampling algorithm is an existing rejective sampling approach). AprAD achieves a trade-off between computation efficiency and keeping unbiased distribution.

### Strengths
## Originality
- The framework of AprAD is original.
- The generalization idea in conclusio is interesting and insightful.

## Clarity
- The algorithm blocks are friendly to readers.
- The intuition is clearly expressed.

## Significance
- AprAD improves the performance and efficiency of constrained decoding.
- The effect shown in Figure 2 looks great.

### Weaknesses
## Major
- Lack of related work. There is no "related work" section. Since the paper has not exceeded the 9-10 page limit, it is strongly recommended to add a "related work" section.
- Lack of novelty. The contribution is a bit marginal, which is an incremental combination of ASAp and speculative decoding. The core idea of combining ASAp with speculative sampling, while practically useful, lacks significant theoretical novelty. The method appears to be a straightforward application of existing techniques rather than a fundamental advancement in the field. The paper does not introduce any new theoretical insights or algorithmic breakthroughs.
- The improvement is not good enough. As can be seen from Table 3, AprAD may underperform ASAp in certain tasks, while only about 1.4 times efficiency improvement. The efficiency gains, while present, are not substantial enough to justify the method's complexity, especially given the performance trade-offs observed in some tasks. The 1.4x speedup is not compelling, particularly when the method does not consistently outperform ASAp.

## Minor
- The title "Approximately Aligned Decoding" is too ambiguous. It would be better to add more descriptions like "constrained", "unbiased", "speculative sampling".

### Questions
- Why does ASAp perform so well in Table 3, while being much worse in Figure 2?

### Soundness
3

### Presentation
1

### Contribution
2
