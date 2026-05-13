# Limits of Deep Learning: Sequence Modeling through the Lens of Complexity Theory

- Decision: Accept
- Scores: 6, 6, 8, 8

## Abstract
Despite their successes, deep learning models struggle with tasks requiring complex reasoning and function composition. We present a theoretical and empirical investigation into the limitations of Structured State Space Models (SSMs) and Transformers in such tasks. We prove that one-layer SSMs cannot efficiently perform function composition over large domains without impractically large state sizes, and even with Chain-of-Thought prompting, they require a number of steps that scale unfavorably with the complexity of the function composition. Multi-layer SSMs are constrained by log-space computational capacity, limiting their reasoning abilities. Our experiments corroborate these theoretical findings. Evaluating models on tasks including various function composition settings, multi-digit multiplication, dynamic programming, and Einstein's puzzle, we find significant performance degradation even with advanced prompting techniques. Models often resort to shortcuts, leading to compounding errors. These findings highlight fundamental barriers within current deep learning architectures rooted in their computational capacities. We underscore the need for innovative solutions to transcend these constraints and achieve reliable multi-step reasoning and compositional task-solving, which is critical for advancing toward general artificial intelligence.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper theoretically and empirically studies the limitations of the computational power of SSMs in terms of effective space complexity and their ability to do function composition.

### Strengths
Novel theoretical insight on the recently popular SSMs (especially in regards to their limited ability to do function composition), echoing similar previous work on Transformers. Experiments validate the theory.

### Weaknesses
1. The proof of Theorem 1 appears to rely on the specific format of the prompt (see Questions below).
2. I have doubts about the correctness of Theorem 4's proof and I don't think the theorem statement itself properly formalizes the insight that it's trying to convey (see Questions below).
3. It seems to me that the criticism in Question 6 below (i.e., that Theorem 4 really says "SSMs' computational power is bounded by the amount of space used to represent floating points") equally applies to the cited papers Merrill & Sabharwal 2023 and Merrill & Sabharwal 2024. Since Theorem 3 is based on the results of the latter paper, it relies on the problematic assumption that precision $p = O(\log N)$. A consequence of this is that changing the assumption on how $p$ scales with $N$ even by a little bit will completely mess up the theorem statement, e.g., if $p = O(\mathrm{poly}(n))$ then we can no longer say that SSMs can't solve these P-complete problems. (See Question 6 below for a more detailed discussion of this point as applied to Theorem 4.)

### Questions
The following questions are about Theorem 1.
1. The proof seems to rely on the specific ordering of $g$ followed by $f$ followed by $x$ in the prompt. Does a similar proof work when these pieces are in different orders? In particular, what about the order that would intuitively be the easiest for the SSM: $x$ followed by $g$ followed by $f$? (The intuition here comes from the fact that a streaming algorithm taking in $(x, g, f)$ in this order wouldn't need to store the entire table of $f$ or $g$.)

The following questions are about Theorem 2.
1. How's the definition of CoT different from just autoregressive decoding?

The following questions are about Theorem 4.
1. Lines 74 & 386: Isn't $\mathsf{L}$ a class of decision problems? Shouldn't one say $\mathsf{FL}$ instead of $\mathsf{L}$ here?
2. How is it possible for $p, d$ to grow with $N$? While an SSM can take an input of variable length $N$, its $p$ and $d$ must be fixed, right? I don't know what it means for the precision and hidden dimension of an SSM to increase as the input sequence becomes longer. SSMs are unlike boolean circuits which require a differently-sized circuit for every possible input size.
3. While the theorem statement assumes $p, d = O(\mathrm{poly}(N))$, the proof assumes $d = O(1), p = O(\log N)$. For example, line 359 says "each element of these matrices can be represented using $O(\log N)$ bits." Line 377 says "numbers are represented with $O(\log N)$ bits of precision." Line 379 says "we only need to keep the current and previous hidden states", which require $O(dp)$ space, hence implicitly assuming $dp = O(\log N)$.
4. How are $A_t, B_t, C_t, D_t$ (which are functions of $x_t$) computed? Some assumption on the space complexity of these computations is missing from the theorem statement.
5. This is a small detail, but in the current formulation where the input sequence is a bunch of vectors of real numbers, I believe the input size is actually $Ndp$. But $O(\log N)$ implies $O(\log(Ndp))$, so there's no problem here even when $dp = \omega(1)$ in $N$.
6. Assuming $A_t, B_t, C_t, D_t$ are independent of the input sequence (and "easily computable"), it's easy to generalize the theorem to say that an SSM with $L$ layers, precision $p$ and hidden dimension $d$ is equivalent to an algorithm that uses $O(Lpd)$ space (i.e., you store hidden states $h_t^{(l)}$ of all layers $l$ at the current time step $t$ and the intermediate result $y_t^{(l_\text{cur})}$ of the current layer $l_\text{cur}$). So Theorem 4's statement that SSMs use log-space is actually just an artifact of $Lpd = O(\log N)$ in the assumption of the (corrected version of the) theorem (see Question 3 above). So it's unclear what insight we get from the fact that SSMs are equivalent to log-space when $Lpd = O(\log N)$. If $p, d = O(1)$ (i.e., the case of actual SSMs), then we get that linear SSMs are equivalent to algorithms that use $O(1)$ space, but does that mean that the decision problems that linear SSMs can solve must be regular languages? (A question of a similar nature: my computer has finite memory, so does that mean it can only decide regular languages?) On the other hand, if $p, d = O(\mathrm{poly}(N))$, then we get that linear SSMs can be simulated by algorithms that use polynomial space, and we no longer get the takeaway that SSMs are limited. To summarize, the fact that the computational power of SSMs (as proven using the method in Theorem 4) varies widely based on what is assumed of the scaling of precision $p$ w.r.t. $N$ indicates a failure of "SSM with precision $p = O(f(N))$" as model to accurately capture the behavior of actual SSMs. Theorem 4 generalized would tell me that an SSM with precision $p = 16N$ can potentially solve P-complete problems and yet an SSM with $p = 64$ can only decide regular languages, but in practice there shouldn't be a difference in what these two classes of SSMs can do. (See below for what I think a theorem statement that actually formalizes the intuitive notion of "SSMs can only compute problems in [complexity class]" might look like.)

Here's my suggestion for how to actually formalize "SSMs only have _____ computational power" into a theorem statement to replace the current Theorem 4.

First, we need to define the inputs and outputs as actual strings, since members of $\mathsf{FL}$ are functions $f : \Sigma^* \to \Sigma^*$. So the input to the SSM is a sequence of tokens $w_1 \ldots w_N$ that first get embedded into vectors $x_t \in \mathbb R^m$ ($t \leq N$), and the output is an argmax applied on top of the last layer of $y_t$'s for $t > N$ until the <eos> token. (The $w_t$ for $t > N$ are the decoded $\arg \max_i (y_{t-1})_i$ as usual.) A basic formalization like this to properly define the inputs/outputs of an SSM is missing from the paper and should be added.

Now, to prevent the issue in Question 6 above where the SSM's computational power ends up being limited by the finite precision in floating point computations, we really should assume infinite precision here. (So we're working with an idealized version of an SSM and not a real one.) And then we can ask about the computational power of an SSM with (given) hidden dimension $d$ and # layers $L$. So the theorem statement looks something like "Functions $f : \Sigma^* \to \Sigma^*$ that can be computed by an infinite-precision SSM with hidden dimension $d$ and # of layers $L$ are within the class _____."

The current proof of Theorem 4 doesn't work anymore, since directly carrying out the computations in the SSM would require infinite space. However, intuitively, SSMs should still be limited in their computational power for the following reason. Since input tokens are discrete, intuitively the spaces of $h_t$ and $y_t$ can, in some sense, be discretized into "regions of equivalent behavior". Thus, if we show that under certain conditions, the space of the hidden state can be divided into a finite number of regions of equivalent behavior, then the SSM is just a finite-state machine and the functions it computes are computable in $O(1)$ space.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper discusses the limitations of the reasoning abilities of SSMs and Transformers. Theoretically, it presents three theorems: (i) the inability of SSMs to efficiently perform function composition; (ii) Chain-of-thought helps yet with exponential increase in reasoning steps; and (iii) the inability of multi-layer SSMs to solve problems that are NL-Complete unless L = N. Empirically, the authors present experiments in qualitative examples of zero-shot inference, function composition, math and other reasoning tasks.

### Strengths
- Originality: This paper precisely defines the problem and proposes new theorems showing new results.
- Clarity and rigor: The theoretical and empirical sections are clearly structured, and concepts are clearly defined. 
- Significance: Reasoning is a crucial problem in this domain. The lower bound on CoT steps required for iterated function composition is an interesting result, showing the practical challenges in scaling up these techniques, which is valuable for the research community. I am not able to verify the proofs, though.
- Empirical evaluation: The empirical results corroborate the theoretical claims effectively. The authors tested various composition tasks (function, spatial, temporal, and relational), presenting concrete evidence of performance degradation across different types of tasks.

### Weaknesses
Note: Unfortunately I am not a domain expert in theoretical computer science, and my evaluations are based on educated guess.

- Could the authors provide an additional section on limitations (of this work per se) and future works, that practitioner may follow? For example, could the authors discuss more specific architectural modifications based on the existing results?
- In practice, complicated reasoning tasks are often solved with (tree) search (cf., [alphaproof](https://deepmind.google/discover/blog/ai-solves-imo-problems-at-silver-medal-level/), [GPT-f](https://arxiv.org/pdf/2009.03393), [HyperTree Search](https://arxiv.org/pdf/2205.11491)), potentially with self-correction (cf., [Self-Correction](https://arxiv.org/pdf/2405.18634), [SCoRe](https://arxiv.org/pdf/2409.12917)), beyond naive stepwise chain-of0thought augmentation. Can the authors provide further discussions on this?

### Questions
See the weakness. I am happy to raise my score if the authors can address the concerns proposed by reviewers.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The core result of this paper is a proof that one-layer structured state space models cannot perform efficient function composition. The paper builds upon prior work from from Christos Papadimitriou in Peng et all who proposed the paradigm. The paper extends results to SSM models and shows that significant COT computation is required to achieve function composition in SSMs. Authors extend analysis to multi layer SSMsdemonstrating that the computation of an L-layer SSM on a prompt of length N can be carried out using O(L log N ) bits of memory, positioning SSMs within the complexity class L (logarithmic space). This implies that SSMs cannot solve problems that are NL-complete unless L = NL, which is widely believed to be false.

### Strengths
Paper is an important contribution as it extends rigorous complexity theory analysis of LLM model limitations to SSM models proving sharp results on resources required to execute function composition.

### Weaknesses
No real weakness. Potentially authors could spend more time comparing their results to Peng for readers.

### Questions
Authors could also clarify the numerical experiments and their relationship to the main theorem with respect to layer number.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors investigate the computational limitations of structured state space models to perform function composition. They provide theoretical and empirical evidence for the infeasibility of these architectures to perform function composition over large domains.

### Strengths
* Well written
* Well referenced
* Settles important questions about the limitations of current architectures of interest for sequence modeling.

This kind of theoretical work is very much needed.

### Weaknesses
 * The main manuscript could use more background on communication complexity concepts and techniques, presented intuitively, to make the methodology and results more accessible to a general ML audience.
* Computational complexity work often must deal with a gap between formal and practical problems (even if the work is conducted rigorously). The paper could use a discussion about this possible gap, the (non-)robustness of the results to closing this gap, and what kind of studies are needed to close this gap.

Since there is still roughly 1 page of extra space before the manuscript reaches the page limit, it would be useful to have more background on the computational complexity concepts and techniques deployed in the proofs. This could include concepts and techniques from communication complexity, relevant problem classes and reducibilities, and the rationale that supports the proofs.

Computational complexity work often must deal with objections related to the gap between theory and practice. It would be useful to elaborate on how these gaps might play out in this work, and what responses to possible objections might look like. For instance, what aspects of the formal definitions might be overly general with respect to a possibly more restricted practical setting? Might such a discrepancy between formalization and practical scenario account for the results? What kind of descriptive empirical work could be needed to close the gap between formal and practical problems?

### Questions
Minor comments and suggestions:

There is a formatting error causing the heading of section 7 to come too close to the previous paragraph.

A summary figure of the empirical results could also be useful in the main manuscript if space limitations allow.

The “Implications for General Artificial Intelligence” paragraph seems more suited to the Conclusions section or a separate “Implications” section than to the “Related Work” section. An Implications section could also elaborate on the links between the formal proofs and the issues of practical interest.

### Soundness
3

### Presentation
3

### Contribution
3
